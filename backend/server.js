const express = require('express');
const axios = require('axios');
const cors = require('cors');

const app = express();
const port = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

let stats = {};
let chart = {};
let problem_dict = {};

const PROBLEM_MODELS_URL = 'https://kenkoooo.com/atcoder/resources/problem-models.json';
const MERGED_PROBLEMS_URL = 'https://kenkoooo.com/atcoder/resources/merged-problems.json';

const get_color = (difficulty) => {
    if (difficulty < 400) return "grey";
    if (difficulty < 800) return "brown";
    if (difficulty < 1200) return "green";
    if (difficulty < 1600) return "cyan";
    if (difficulty < 2000) return "blue";
    if (difficulty < 2400) return "yellow";
    if (difficulty < 2800) return "orange";
    if (difficulty < 3200) return "red";
    return "black";
};

const fetchData = async () => {
    try {
        console.log('Fetching data...');
        const [problemModelsResponse, mergedProblemsResponse] = await Promise.all([
            axios.get(PROBLEM_MODELS_URL),
            axios.get(MERGED_PROBLEMS_URL)
        ]);

        const problemModels = problemModelsResponse.data;
        const mergedProblems = mergedProblemsResponse.data;

        console.log('Processing data...');
        // Initialize stats
        stats = {
            count: 0,
            ac_count: 0,
            unique_ac_count: 0,
            difficulty_sum: 0,
            difficulty_avg: 0,
            problem_count: 0,
            problem_ac_count: 0,
            problem_unique_ac_count: 0,
        };

        // Initialize chart
        chart = {
            grey: { total: 0, ac: 0 },
            brown: { total: 0, ac: 0 },
            green: { total: 0, ac: 0 },
            cyan: { total: 0, ac: 0 },
            blue: { total: 0, ac: 0 },
            yellow: { total: 0, ac: 0 },
            orange: { total: 0, ac: 0 },
            red: { total: 0, ac: 0 },
            black: { total: 0, ac: 0 }
        };
        
        problem_dict = {};

        mergedProblems.forEach(problem => {
            const problemId = problem.id;
            const difficulty = problemModels[problemId]?.difficulty;

            if (difficulty === undefined) return; // Skip if no difficulty

            const color = get_color(difficulty);
            chart[color].total++;
            stats.problem_count++;

            problem_dict[problemId] = {
                ...problem,
                difficulty: difficulty,
                color: color,
                // Assuming 'status' and 'epoch_second' are properties of problem if it's solved
                // These would typically come from user submission data, not merged-problems.json
                // For now, let's simulate this based on some criteria or leave as placeholders
                status: null, 
                epoch_second: null 
            };
        });
        
        // The following parts from dict.py (user submissions) are not directly applicable here
        // as we don't have user submission data.
        // We are mainly focused on creating the problem_dict with difficulties and colors.
        // stats calculation related to user ACs will be different or removed.

        console.log('Data fetched and processed successfully.');

    } catch (error) {
        console.error('Error fetching or processing data:', error.message);
        // Consider more robust error handling or retry mechanisms
    }
};


// API Endpoints
app.get('/api/stats', (req, res) => {
    res.json(stats);
});

app.get('/api/chart', (req, res) => {
    res.json(chart);
});

app.get('/api/problem_dict', (req, res) => {
    res.json(problem_dict);
});

app.get('/api/all_data', (req, res) => {
    res.json({
        stats,
        chart,
        problem_dict
    });
});

// Start server and fetch data
app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
    fetchData(); // Fetch data when server starts
});
