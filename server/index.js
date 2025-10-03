const express = require('express');
const axios = require('axios');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, '../dist')));
app.use('/web-page', express.static(path.join(__dirname, '../web-page')));

// Color thresholds matching the Python implementation
const COLOR_THRESHOLDS = [
  { threshold: 400, color: 'grey' },
  { threshold: 800, color: 'brown' },
  { threshold: 1200, color: 'green' },
  { threshold: 1600, color: 'cyan' },
  { threshold: 2000, color: 'blue' },
  { threshold: 2400, color: 'yellow' },
  { threshold: 2800, color: 'orange' },
  { threshold: 3200, color: 'red' },
  { threshold: 3600, color: 'bronze' },
  { threshold: 4000, color: 'silver' },
  { threshold: 4400, color: 'gold' }
];

function getColor(difficulty) {
  if (difficulty === null || difficulty === undefined) {
    return null;
  }
  for (const { threshold, color } of COLOR_THRESHOLDS) {
    if (difficulty < threshold) {
      return color;
    }
  }
  return 'red';
}

// API endpoint to fetch and process AtCoder data
app.get('/api/data', async (req, res) => {
  try {
    console.log('Fetching data from AtCoder API...');
    
    // Fetch data from AtCoder API
    const [problemModelsResponse, mergedProblemsResponse] = await Promise.all([
      axios.get('https://kenkoooo.com/atcoder/resources/problem-models.json'),
      axios.get('https://kenkoooo.com/atcoder/resources/merged-problems.json')
    ]);

    const problemModels = problemModelsResponse.data;
    const mergedProblems = mergedProblemsResponse.data;

    console.log(`Loaded ${Object.keys(problemModels).length} problem models`);
    console.log(`Loaded ${mergedProblems.length} merged problems`);

    // Initialize data structures
    const stats = { abc: {}, arc: {}, agc: {}, others: {} };
    const chart = { abc: {}, arc: {}, agc: {}, others: {} };
    const problemDict = { abc: {}, arc: {}, agc: {}, others: {} };

    // Process each problem
    for (const problem of mergedProblems) {
      let contestType;
      if (problem.contest_id.includes('abc')) {
        contestType = 'abc';
      } else if (problem.contest_id.includes('arc')) {
        contestType = 'arc';
      } else if (problem.contest_id.includes('agc')) {
        contestType = 'agc';
      } else {
        contestType = 'others';
      }

      const contestId = problem.contest_id;
      const problemId = problem.id;

      // Initialize contest entry if needed
      if (!stats[contestType][contestId]) {
        stats[contestType][contestId] = {};
      }

      stats[contestType][contestId][problemId] = {
        name: problem.name,
        point: problem.point,
        solver_count: problem.solver_count
      };

      // Add problem model data if available
      if (problemModels[problemId]) {
        const model = problemModels[problemId];
        if (model.is_experimental !== undefined) {
          stats[contestType][contestId][problemId].is_experimental = model.is_experimental;
        }
        if (model.variance !== undefined) {
          stats[contestType][contestId][problemId].variance = model.variance;
        }
        if (model.difficulty !== undefined) {
          stats[contestType][contestId][problemId].difficulty = model.difficulty;
          const color = getColor(model.difficulty);
          if (color) {
            stats[contestType][contestId][problemId].color = color;
          }
        }
      }
    }

    // Build chart data: count problems by point and color
    for (const contestType in stats) {
      for (const contestId in stats[contestType]) {
        for (const problemId in stats[contestType][contestId]) {
          const problem = stats[contestType][contestId][problemId];
          if (problem.color && problem.point !== null && problem.point !== undefined) {
            const point = problem.point;
            const color = problem.color;
            
            if (!chart[contestType][point]) {
              chart[contestType][point] = {};
            }
            chart[contestType][point][color] = (chart[contestType][point][color] || 0) + 1;

            // Build problem dictionary
            if (!problemDict[contestType][point]) {
              problemDict[contestType][point] = {};
            }
            if (!problemDict[contestType][point][color]) {
              problemDict[contestType][point][color] = [];
            }
            problemDict[contestType][point][color].push(problemId);
          }
        }
      }
    }

    console.log('Data processed successfully');
    res.json({ stats, chart, problemDict });
  } catch (error) {
    console.error('Error fetching data:', error.message);
    res.status(500).json({ error: 'Failed to fetch data from AtCoder API' });
  }
});

// Serve React app for all other routes (excluding API and static assets)
app.get('*', (req, res, next) => {
  if (req.path.startsWith('/api') || req.path.startsWith('/assets') || req.path.startsWith('/web-page')) {
    return next();
  }
  res.sendFile(path.join(__dirname, '../dist/index.html'));
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
