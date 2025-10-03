import React, { useEffect, useRef } from 'react';
import { Link } from 'react-router-dom';

const COLOR_ORDER = ['grey', 'brown', 'green', 'cyan', 'blue', 'yellow', 'orange', 'red', 'bronze', 'silver', 'gold'];

function StatsTable({ stats, contestType, active }) {
  const tableRef = useRef(null);

  useEffect(() => {
    if (active && tableRef.current) {
      const rows = tableRef.current.querySelectorAll('tbody tr');
      rows.forEach((row, index) => {
        row.style.animation = 'none';
        setTimeout(() => {
          row.style.animation = `fadeInUp 0.5s ease-out ${index * 0.05}s both`;
        }, 10);
      });

      // Initialize progress circles
      const circles = tableRef.current.querySelectorAll('.progress-circle');
      circles.forEach((circle) => {
        const percent = parseFloat(circle.getAttribute('data-percent'));
        const color = circle.getAttribute('data-color');
        const circumference = 2 * Math.PI * 45;
        const offset = circumference - (percent / 100) * circumference;
        
        circle.style.setProperty('--circle-color', color);
        circle.style.setProperty('--circle-offset', offset);
      });
    }
  }, [active]);

  const sortedPoints = Object.keys(stats).sort((a, b) => parseFloat(a) - parseFloat(b));

  return (
    <div className={`tab-content ${active ? 'active' : ''}`} id={`table-${contestType}`}>
      <div className="table-responsive">
        <table className="stats-table" ref={tableRef}>
          <thead>
            <tr>
              <th>Score</th>
              {COLOR_ORDER.map(color => (
                <th key={color}>{color.charAt(0).toUpperCase() + color.slice(1)}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {sortedPoints.map((point) => {
              const colorCounts = stats[point];
              const total = Object.values(colorCounts).reduce((sum, count) => sum + count, 0) || 1;
              const pointInt = parseInt(parseFloat(point));

              return (
                <tr key={point}>
                  <td className="score-label">{pointInt}</td>
                  {COLOR_ORDER.map((color) => {
                    const count = colorCounts[color] || 0;
                    const percent = Math.round((count / total) * 100 * 100) / 100;
                    const circleClass = count > 0 ? `color-${color}` : 'empty-color';
                    const bgClass = count > 0 ? `bg-${color}` : '';

                    return (
                      <td key={color}>
                        {count > 0 ? (
                          <Link to={`/lists/${contestType}/${pointInt}/${color}`} className="box-link">
                            <div className="stats-container">
                              <div className="circle-container">
                                <div
                                  className={`progress-circle ${circleClass}`}
                                  data-color={`var(--${color})`}
                                  data-percent={percent}
                                >
                                  <span className={`progress-circle-inner ${bgClass}`}></span>
                                </div>
                                <span className={`count ${circleClass}`}>{count}</span>
                              </div>
                              <span className={`percentage ${circleClass}`}>({percent}%)</span>
                            </div>
                          </Link>
                        ) : (
                          <div className="stats-container">
                            <div className="circle-container">
                              <div
                                className={`progress-circle ${circleClass}`}
                                data-color={`var(--${color})`}
                                data-percent={percent}
                              >
                                <span className={`progress-circle-inner ${bgClass}`}></span>
                              </div>
                              <span className={`count ${circleClass}`}>{count}</span>
                            </div>
                            <span className={`percentage ${circleClass}`}>({percent}%)</span>
                          </div>
                        )}
                      </td>
                    );
                  })}
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default StatsTable;
