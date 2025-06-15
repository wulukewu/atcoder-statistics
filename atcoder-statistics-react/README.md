### Step 1: Set Up Your React Environment

1. **Install Node.js and npm**: Make sure you have Node.js and npm installed on your machine. You can download it from [Node.js official website](https://nodejs.org/).

2. **Create a New React App**: Use Create React App to set up your project. Open your terminal and run:
   ```bash
   npx create-react-app atcoder-statistics
   cd atcoder-statistics
   ```

### Step 2: Install Required Packages

You may need some additional packages for routing and making HTTP requests. Install them using npm:
```bash
npm install axios react-router-dom
```

### Step 3: Project Structure

Create the following folder structure inside the `src` directory:

```
src/
├── components/
│   ├── Header.js
│   ├── ProblemList.js
│   ├── ProblemCard.js
│   ├── StatisticsTable.js
│   └── ThemeToggle.js
├── pages/
│   ├── Home.js
│   └── ProblemPage.js
├── App.js
├── index.js
└── api.js
```

### Step 4: Create API Functions

Create a file named `api.js` to handle API requests:

```javascript
// src/api.js
import axios from 'axios';

const BASE_URL = 'https://kenkoooo.com/atcoder/resources';

export const fetchProblemModels = async () => {
    const response = await axios.get(`${BASE_URL}/problem-models.json`);
    return response.data;
};

export const fetchMergedProblems = async () => {
    const response = await axios.get(`${BASE_URL}/merged-problems.json`);
    return response.data;
};
```

### Step 5: Create Components

#### Header Component

```javascript
// src/components/Header.js
import React from 'react';

const Header = () => {
    return (
        <header>
            <h1>AtCoder Statistics</h1>
        </header>
    );
};

export default Header;
```

#### Problem Card Component

```javascript
// src/components/ProblemCard.js
import React from 'react';

const ProblemCard = ({ problem }) => {
    return (
        <div className="problem-card">
            <h3>{problem.name}</h3>
            <p>Point: {problem.point}</p>
            <p>Solvers: {problem.solver_count}</p>
            <a href={`https://atcoder.jp/contests/${problem.contest_id}/tasks/${problem.id}`} target="_blank" rel="noopener noreferrer">Open</a>
        </div>
    );
};

export default ProblemCard;
```

#### Problem List Component

```javascript
// src/components/ProblemList.js
import React from 'react';
import ProblemCard from './ProblemCard';

const ProblemList = ({ problems }) => {
    return (
        <div className="problem-list">
            {problems.map(problem => (
                <ProblemCard key={problem.id} problem={problem} />
            ))}
        </div>
    );
};

export default ProblemList;
```

#### Statistics Table Component

```javascript
// src/components/StatisticsTable.js
import React from 'react';

const StatisticsTable = ({ stats }) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>Contest Type</th>
                    <th>Contests</th>
                    <th>Problems</th>
                </tr>
            </thead>
            <tbody>
                {Object.entries(stats).map(([type, data]) => (
                    <tr key={type}>
                        <td>{type.toUpperCase()}</td>
                        <td>{data.contests}</td>
                        <td>{data.problems}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    );
};

export default StatisticsTable;
```

#### Theme Toggle Component

```javascript
// src/components/ThemeToggle.js
import React from 'react';

const ThemeToggle = ({ toggleTheme }) => {
    return (
        <button onClick={toggleTheme}>Toggle Theme</button>
    );
};

export default ThemeToggle;
```

### Step 6: Create Pages

#### Home Page

```javascript
// src/pages/Home.js
import React, { useEffect, useState } from 'react';
import { fetchProblemModels, fetchMergedProblems } from '../api';
import Header from '../components/Header';
import ProblemList from '../components/ProblemList';
import StatisticsTable from '../components/StatisticsTable';

const Home = () => {
    const [problems, setProblems] = useState([]);
    const [stats, setStats] = useState({});

    useEffect(() => {
        const loadData = async () => {
            const problemModels = await fetchProblemModels();
            const mergedProblems = await fetchMergedProblems();
            // Process data to set problems and stats
            setProblems(mergedProblems);
            // Set stats based on your logic
            setStats({
                abc: { contests: 10, problems: 50 },
                arc: { contests: 8, problems: 40 },
                agc: { contests: 5, problems: 30 },
            });
        };
        loadData();
    }, []);

    return (
        <div>
            <Header />
            <StatisticsTable stats={stats} />
            <ProblemList problems={problems} />
        </div>
    );
};

export default Home;
```

### Step 7: Set Up Routing

Modify `App.js` to set up routing:

```javascript
// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './pages/Home';

const App = () => {
    return (
        <Router>
            <Switch>
                <Route path="/" component={Home} />
            </Switch>
        </Router>
    );
};

export default App;
```

### Step 8: Style Your Application

You can add CSS styles in `src/App.css` or create a new CSS file for each component. For example:

```css
/* src/App.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f8fdfa;
    color: #343a40;
}

header {
    background: linear-gradient(135deg, #0f9d58, #0b7d46);
    color: white;
    padding: 1.5rem;
    text-align: center;
}

.problem-card {
    border: 1px solid #dee2e6;
    border-radius: 0.75rem;
    padding: 1rem;
    margin: 1rem 0;
}

.problem-list {
    display: flex;
    flex-direction: column;
}
```

### Step 9: Run Your Application

Finally, run your application using:

```bash
npm start
```

This will start the development server, and you can view your application in your browser at `http://localhost:3000`.

### Conclusion

This setup provides a basic structure for your AtCoder Statistics web application using React. You can further enhance it by adding features like theming, detailed problem views, and more sophisticated state management using tools like Redux or Context API.