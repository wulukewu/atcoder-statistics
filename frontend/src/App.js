import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [chart, setChart] = useState(null);
  const [activeTab, setActiveTab] = useState('abc');

  useEffect(() => {
    fetch('http://localhost:8000/json/chart.json')
      .then(res => res.json())
      .then(data => setChart(data));
  }, []);

  const getAllColors = (scores) => {
    const colorSet = new Set();
    Object.values(scores).forEach(colors =>
      Object.keys(colors).forEach(color => colorSet.add(color))
    );
    return Array.from(colorSet);
  };

  const tabList = [
    { key: 'abc', label: 'AtCoder Beginner Contest' },
    { key: 'arc', label: 'AtCoder Regular Contest' },
    { key: 'agc', label: 'AtCoder Grand Contest' }
  ];

  return (
    <div className="App">
      <div className="card">
        <div className="card-header">
          <div className="card-title">AtCoder Problems</div>
        </div>
        <div className="tabs">
          {tabList.map(tab => (
            <div
              key={tab.key}
              className={`tab${activeTab === tab.key ? ' active' : ''}`}
              onClick={() => setActiveTab(tab.key)}
            >
              {tab.label}
            </div>
          ))}
        </div>
        <div className="tables">
          {tabList.map(tab => (
            <div
              key={tab.key}
              className={`tab-content${activeTab === tab.key ? ' active' : ''}`}
              style={{ display: activeTab === tab.key ? 'block' : 'none' }}
            >
              <div className="table-responsive">
                {chart && chart[tab.key] ? (
                  <table className="stats-table">
                    <thead>
                      <tr>
                        <th>Score</th>
                        {getAllColors(chart[tab.key]).map(color => (
                          <th key={color}>{color.charAt(0).toUpperCase() + color.slice(1)}</th>
                        ))}
                      </tr>
                    </thead>
                      <tbody>
                        {Object.entries(chart[tab.key]).map(([score, colors], rowIdx) => {
                          const total = Object.values(colors).reduce((a, b) => a + b, 0);
                          return (
                            <tr key={score}>
                              <td className="score-label">{score}</td>
                              {getAllColors(chart[tab.key]).map(color => {
                                const amount = colors[color] || 0;
                                const percent = total ? ((amount / total) * 100).toFixed(2) : "0.00";
                                // Make clipPath id unique
                                const clipId = `clip-${tab.key}-${score}-${color}-${rowIdx}`;
                                return (
                                  <td key={color}>
                                    <div className={`stats-container${amount === 0 ? ' zero-amount' : ''}`}>
                                      <svg
                                        width="16"
                                        height="16"
                                        viewBox="0 0 16 16"
                                        className={`progress-cup color-${color}${amount === 0 ? ' zero-amount' : ''}`}
                                        style={{ marginBottom: 2 }}
                                      >
                                        <defs>
                                          <clipPath id={clipId}>
                                            <circle cx="8" cy="8" r="7" />
                                          </clipPath>
                                        </defs>
                                        {/* Hollow circle border */}
                                        <circle
                                          cx="8"
                                          cy="8"
                                          r="7"
                                          fill="none"
                                          stroke="#e5e7eb"
                                          strokeWidth="2"
                                        />
                                        {/* Filled part, from bottom up */}
                                        <rect
                                          x="1"
                                          y={16 - 14 * (amount / (total || 1))}
                                          width="14"
                                          height={14 * (amount / (total || 1))}
                                          fill={amount === 0 ? "#f3f4f6" : "currentColor"}
                                          clipPath={`url(#${clipId})`}
                                          style={{ transition: 'y 0.5s, height 0.5s' }}
                                        />
                                      </svg>
                                      <span className={`count color-${color}${amount === 0 ? ' zero-amount' : ''}`}>{amount}</span>
                                      <span className={`percentage color-${color}${amount === 0 ? ' zero-amount' : ''}`}>({percent}%)</span>
                                    </div>
                                  </td>
                                );
                              })}
                            </tr>
                          );
                        })}
                      </tbody>
                  </table>
                ) : (
                  <div>Loading...</div>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;