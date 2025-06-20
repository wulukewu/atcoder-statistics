const fetch = require("node-fetch");
const fs = require("fs");
const path = require("path");

const COLOR_THRESHOLDS = [
  [400, "grey"],
  [800, "brown"],
  [1200, "green"],
  [1600, "cyan"],
  [2000, "blue"],
  [2400, "yellow"],
  [2800, "orange"],
  [3200, "red"],
  [3600, "bronze"],
  [4000, "silver"],
  [4400, "gold"],
];

function getColor(difficulty) {
  if (difficulty === undefined || difficulty === null) return null;
  for (const [threshold, color] of COLOR_THRESHOLDS) {
    if (difficulty < threshold) return color;
  }
  return "red";
}

async function collectData(saveDir) {
  // Fetch data
  const problemModels = await fetch(
    "https://kenkoooo.com/atcoder/resources/problem-models.json"
  ).then((res) => res.json());
  const mergedProblems = await fetch(
    "https://kenkoooo.com/atcoder/resources/merged-problems.json"
  ).then((res) => res.json());

  // Initialize data structures
  const stats = { abc: {}, arc: {}, agc: {}, others: {} };
  const chart = { abc: {}, arc: {}, agc: {}, others: {} };
  const problemDict = { abc: {}, arc: {}, agc: {}, others: {} };
  const contestCounts = { abc: 0, arc: 0, agc: 0, others: 0 };
  const problemCounts = { abc: 0, arc: 0, agc: 0, others: 0 };

  // Process problems
  for (const problem of mergedProblems) {
    let contestType = "others";
    if (problem.contest_id.includes("abc")) contestType = "abc";
    else if (problem.contest_id.includes("arc")) contestType = "arc";
    else if (problem.contest_id.includes("agc")) contestType = "agc";
    const contestId = problem.contest_id;
    const problemId = problem.id;

    if (!stats[contestType][contestId]) {
      stats[contestType][contestId] = {};
      contestCounts[contestType]++;
    }
    stats[contestType][contestId][problemId] = {
      name: problem.name,
      point: problem.point,
      solver_count: problem.solver_count,
    };
    problemCounts[contestType]++;

    // Add problem model data if available
    if (problemModels[problemId]) {
      const model = problemModels[problemId];
      if ("is_experimental" in model)
        stats[contestType][contestId][problemId].is_experimental =
          model.is_experimental;
      if ("variance" in model)
        stats[contestType][contestId][problemId].variance = model.variance;
      if ("difficulty" in model) {
        stats[contestType][contestId][problemId].difficulty = model.difficulty;
        const color = getColor(model.difficulty);
        if (color) stats[contestType][contestId][problemId].color = color;
      }
    }
  }

  // Build chart data
  for (const contestType in stats) {
    for (const contestId in stats[contestType]) {
      for (const problemId in stats[contestType][contestId]) {
        const problem = stats[contestType][contestId][problemId];
        if (
          !problem.color ||
          problem.point === undefined ||
          problem.point === null
        )
          continue;
        const point = problem.point;
        const color = problem.color;
        if (!chart[contestType][point]) chart[contestType][point] = {};
        chart[contestType][point][color] =
          (chart[contestType][point][color] || 0) + 1;
      }
    }
  }

  // Build problemDict
  for (const contestType in stats) {
    for (const contestId in stats[contestType]) {
      for (const problemId in stats[contestType][contestId]) {
        const problem = stats[contestType][contestId][problemId];
        if (
          !problem.color ||
          problem.point === undefined ||
          problem.point === null
        )
          continue;
        const point = problem.point;
        const color = problem.color;
        if (!problemDict[contestType][point])
          problemDict[contestType][point] = {};
        if (!problemDict[contestType][point][color])
          problemDict[contestType][point][color] = [];
        problemDict[contestType][point][color].push(problemId);
      }
    }
  }

  // Ensure output directory exists
  if (!fs.existsSync(saveDir)) fs.mkdirSync(saveDir, { recursive: true });

  // Save files
  fs.writeFileSync(
    path.join(saveDir, "stats.json"),
    JSON.stringify(stats, null, 2)
  );
  fs.writeFileSync(
    path.join(saveDir, "chart.json"),
    JSON.stringify(chart, null, 2)
  );
  fs.writeFileSync(
    path.join(saveDir, "problem_dict.json"),
    JSON.stringify(problemDict, null, 2)
  );

  return {
    stats: path.join(saveDir, "stats.json"),
    chart: path.join(saveDir, "chart.json"),
    problem_dict: path.join(saveDir, "problem_dict.json"),
  };
}

function readJsonFile(dir, filename) {
  const filePath = path.join(dir, filename);
  if (!fs.existsSync(filePath)) return null;
  return fs.readFileSync(filePath, "utf-8");
}

module.exports = { collectData, readJsonFile };
