import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { fetchAtCoderData } from '../utils/api';
import { initializeTheme, toggleTheme, cycleColorTheme } from '../utils/theme';

function ProblemList() {
  const { contestType, point, color } = useParams();
  const [problems, setProblems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [mode, setMode] = useState('dark');

  useEffect(() => {
    const { mode: initialMode } = initializeTheme();
    setMode(initialMode);

    async function loadProblems() {
      try {
        const data = await fetchAtCoderData();
        const problemIds = data.problemDict[contestType]?.[point]?.[color] || [];
        
        // Sort problem IDs in reverse order (newest first)
        problemIds.sort().reverse();
        
        // Get problem details
        const problemDetails = [];
        for (const problemId of problemIds) {
          // Find the contest containing this problem
          for (const contestId in data.stats[contestType]) {
            if (data.stats[contestType][contestId][problemId]) {
              const problem = data.stats[contestType][contestId][problemId];
              const contestTag = contestId.toUpperCase() + problemId.split('_').pop().toUpperCase();
              
              problemDetails.push({
                id: problemId,
                contestId,
                name: problem.name,
                tag: contestTag,
                url: `https://atcoder.jp/contests/${contestId}/tasks/${problemId}`
              });
              break;
            }
          }
        }
        
        setProblems(problemDetails);
        setLoading(false);
      } catch (err) {
        console.error('Error loading problems:', err);
        setLoading(false);
      }
    }

    loadProblems();
  }, [contestType, point, color]);

  const handleToggleTheme = () => {
    const newMode = toggleTheme();
    setMode(newMode);
  };

  const handleCycleColorTheme = () => {
    cycleColorTheme();
  };

  if (loading) {
    return (
      <div className="container">
        <div className="problem-list-container">
          <div className="problem-list-header">
            <h1>Loading...</h1>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="container">
      <div className="problem-list-container">
        <div className="problem-list-header">
          <h1 className="problem-list-title">
            {contestType.toUpperCase()} - {point} points - {color.charAt(0).toUpperCase() + color.slice(1)}
          </h1>
          <p className="problem-count">{problems.length} problems</p>
        </div>
        
        <div className="problem-grid">
          {problems.map((problem) => (
            <div key={problem.id} className="problem-card">
              <div className="problem-header">
                <span className="problem-title">{problem.name}</span>
                <span className={`problem-badge color-${color}`}>{color}</span>
              </div>
              <div className="problem-meta">
                <span className="problem-id">{problem.tag}</span>
                <a href={problem.url} target="_blank" rel="noopener noreferrer" className="external-link">
                  Open
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M14 3h7m0 0v7m0-7L10 14m-4 0h4v4"/>
                  </svg>
                </a>
              </div>
            </div>
          ))}
        </div>
      </div>

      <Link to="/" className="floating-button home-button">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          width="24"
          height="24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="2"
            d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
          />
        </svg>
      </Link>

      <div className="theme-toggle" onClick={handleToggleTheme}>
        <svg
          className="sun-icon"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          width="24"
          height="24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="2"
            d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"
          />
        </svg>
        <svg
          className="moon-icon"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          width="24"
          height="24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="2"
            d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"
          />
        </svg>
      </div>

      <div className="color-theme-toggle" onClick={handleCycleColorTheme}>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          width="24"
          height="24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="2"
            d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01"
          />
        </svg>
      </div>
    </div>
  );
}

export default ProblemList;
