const express = require('express');
const axios = require('axios');
const cors = require('cors');

const app = express();
// Vercel will set the PORT environment variable.
// No need to define a default port for app.listen, as Vercel handles this.

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
        console.log('Fetching data for Vercel serverless function...');
        const [problemModelsResponse, mergedProblemsResponse] = await Promise.all([
            axios.get(PROBLEM_MODELS_URL),
            axios.get(MERGED_PROBLEMS_URL)
        ]);

        const problemModels = problemModelsResponse.data;
        const mergedProblems = mergedProblemsResponse.data;

        console.log('Processing data for Vercel serverless function...');
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
                status: null, 
                epoch_second: null 
            };
        });
        
        console.log('Data fetched and processed successfully for Vercel.');

    } catch (error) {
        console.error('Error fetching or processing data for Vercel:', error.message);
        // In a serverless environment, this error might cause the function to fail on cold start.
        // Consider fallback strategies or error reporting.
    }
};

// Fetch data when the module is loaded (serverless function initializes)
fetchData();

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

// Export the app for Vercel
module.exports = app;
