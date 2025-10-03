import React, { useState, useEffect } from 'react';
import { fetchAtCoderData } from '../utils/api';
import { initializeTheme, toggleTheme, cycleColorTheme } from '../utils/theme';
import StatsTable from './StatsTable';

const COLOR_ORDER = ['grey', 'brown', 'green', 'cyan', 'blue', 'yellow', 'orange', 'red', 'bronze', 'silver', 'gold'];

function Dashboard() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [activeTab, setActiveTab] = useState('table-abc');
  const [latestContests, setLatestContests] = useState({});
  const [mode, setMode] = useState('dark');

  useEffect(() => {
    const { mode: initialMode } = initializeTheme();
    setMode(initialMode);

    async function loadData() {
      try {
        const result = await fetchAtCoderData();
        setData(result);
        
        // Find latest contests
        const latest = {};
        for (const contestType of ['abc', 'arc', 'agc']) {
          const contests = Object.keys(result.stats[contestType]).reverse();
          for (const contestId of contests) {
            const problems = result.stats[contestType][contestId];
            const hasColoredProblem = Object.values(problems).some(
              p => p.color && p.point !== null && p.point !== undefined
            );
            if (hasColoredProblem) {
              latest[contestType] = contestId.toUpperCase();
              break;
            }
          }
          if (!latest[contestType]) {
            latest[contestType] = 'N/A';
          }
        }
        setLatestContests(latest);
        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    }

    loadData();
  }, []);

  const handleToggleTheme = () => {
    const newMode = toggleTheme();
    setMode(newMode);
  };

  const handleCycleColorTheme = () => {
    cycleColorTheme();
  };

  const aggregateStats = (contestType) => {
    if (!data) return {};
    
    const stats = {};
    const chartData = data.chart[contestType];
    
    for (const point in chartData) {
      stats[point] = {};
      COLOR_ORDER.forEach(color => {
        stats[point][color] = chartData[point][color] || 0;
      });
    }
    
    return stats;
  };

  const handleTabChange = (tabId) => {
    setActiveTab(tabId);
  };

  if (loading) {
    return (
      <div className="container">
        <div className="dashboard">
          <div className="header">
            <h1 className="title">Loading...</h1>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="container">
        <div className="dashboard">
          <div className="header">
            <h1 className="title">Error</h1>
            <p>Failed to load data: {error}</p>
          </div>
        </div>
      </div>
    );
  }

  const getLatestForTab = () => {
    if (activeTab === 'table-abc') return latestContests.abc || 'N/A';
    if (activeTab === 'table-arc') return latestContests.arc || 'N/A';
    if (activeTab === 'table-agc') return latestContests.agc || 'N/A';
    return 'N/A';
  };

  return (
    <div className="container">
      <div className="dashboard">
        <div className="header">
          <div className="logo-container">
            <img
              src="/web-page/atcoder-problems-logo.png"
              alt="AtCoder Problems Logo"
              className="logo"
            />
          </div>
          <h1 className="title">AtCoder Statistics</h1>
          <p className="subtitle">Problem Distribution by Difficulty Rating</p>
          <p id="latest-contest-label" className="latest-contest"
             data-latest-abc={latestContests.abc}
             data-latest-arc={latestContests.arc}
             data-latest-agc={latestContests.agc}>
            Latest Contest: {getLatestForTab()}
          </p>
        </div>
        
        <div className="content">
          <div className="tabs">
            <button
              className={`tab ${activeTab === 'table-abc' ? 'active' : ''}`}
              onClick={() => handleTabChange('table-abc')}
              data-tab="table-abc"
            >
              ABC
            </button>
            <button
              className={`tab ${activeTab === 'table-arc' ? 'active' : ''}`}
              onClick={() => handleTabChange('table-arc')}
              data-tab="table-arc"
            >
              ARC
            </button>
            <button
              className={`tab ${activeTab === 'table-agc' ? 'active' : ''}`}
              onClick={() => handleTabChange('table-agc')}
              data-tab="table-agc"
            >
              AGC
            </button>
          </div>

          <div className="tab-contents">
            <StatsTable
              stats={aggregateStats('abc')}
              contestType="abc"
              active={activeTab === 'table-abc'}
              problemDict={data?.problemDict.abc}
              statsData={data?.stats.abc}
            />
            <StatsTable
              stats={aggregateStats('arc')}
              contestType="arc"
              active={activeTab === 'table-arc'}
              problemDict={data?.problemDict.arc}
              statsData={data?.stats.arc}
            />
            <StatsTable
              stats={aggregateStats('agc')}
              contestType="agc"
              active={activeTab === 'table-agc'}
              problemDict={data?.problemDict.agc}
              statsData={data?.stats.agc}
            />
          </div>
        </div>
      </div>

      <div
        className="floating-button"
        onClick={() => window.open('https://kenkoooo.com/atcoder/#/table', '_blank')}
      >
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
            d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"
          />
        </svg>
      </div>

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

export default Dashboard;
