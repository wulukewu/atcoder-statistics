// import React from 'react';

const COLOR_ORDER = [
  "grey",
  "brown",
  "green",
  "cyan",
  "blue",
  "yellow",
  "orange",
  "red",
  "bronze",
  "silver",
  "gold",
];

const COLOR_LABELS = {
  grey: "Grey",
  brown: "Brown",
  green: "Green",
  cyan: "Cyan",
  blue: "Blue",
  yellow: "Yellow",
  orange: "Orange",
  red: "Red",
  bronze: "bronze",
  silver: "silver",
  gold: "gold",
};

function Amount({color, amount}) {
  return(
    <span
      className={`count${
        amount === 0
          ? " color-grey empty-color"
          : ` color-${color}`
      }${
        amount === 0
          ? " zero-amount"
          : ""
      }`}
    >
      {amount}
    </span>
  );
}

function Percent({ percent , amount, color }) {
  return(
    <span
      className={`percentage${
        amount === 0
          ? " color-grey empty-color"
          : ` color-${color}`
      }${
        amount === 0 ? " zero-amount" : ""
      }`}
    >
      ({percent}%)
    </span>
  );
}

function UpperStat({ color, amount, percent }) {
  return(
    <div className="stats-main">
      <div
        className={`progress-circle${
          amount === 0
            ? " color-grey empty-color"
            : ` color-${color}`
        }${
          amount === 0
            ? " zero-amount"
            : ""
        }`}
        data-color={`var(--${color})`}
        data-percent={percent}
      >
        <span
          className={`progress-circle-inner bg-${color}`}
          style={{
            height: `${percent}%`,
          }}
        ></span>
      </div>
      <Amount
        color={color}
        amount={amount}
      />
    </div>
  );
}

function Colums({ color, amount, percent, rowIndex }) {
    return (
        <td key={color}>
            <div
            className="fade-row"
            style={{
                animation: "fadeInUp 0.5s ease forwards",
                animationDelay: `${rowIndex * 0.1}s`,
                opacity: 0,
            }}
            >
            <div className={`stats-container${amount === 0 ? " zero-amount" : ""}`}>
                <UpperStat color={color} amount={amount} percent={percent} />
                <Percent percent={percent} amount={amount} color={color} />
            </div>
            </div>
        </td>
    );
}

function Rows({ score, colors, total, rowIndex }) {
    return(
        <tr key={score}>
        <td>
          <div
            className="fade-row"
            style={{
              animation: "fadeInUp 0.5s ease forwards",
              animationDelay: `${rowIndex * 0.1}s`,
              opacity: 0,
            }}
          >
            <span className="score-label">{score}</span>
          </div>
        </td>
        {COLOR_ORDER.map((color) => {
          const amount = colors[color] || 0;
          const percent = total ? ((amount / total) * 100).toFixed(2) : "0.00";
          return (
            <Colums 
                key={color}
                color={color}
                amount={amount}
                percent={percent}
                rowIndex={rowIndex}
            />
          );
        })}
      </tr>
    );
}

function renderAnimatedRows(chart, tab) {
  if (!chart || !chart[tab.key]) return null;
  return Object.entries(chart[tab.key]).map(([score, colors], rowIndex) => {
    const total = Object.values(colors).reduce((a, b) => a + b, 0);
    return (
      <Rows
        key={score}
        score={score}
        colors={colors}
        total={total}
        rowIndex={rowIndex}
      />
    );
  });
}

function Table({ tab, chart }) {
  return (
    <div className="table-responsive">
      <table className="stats-table">
        <thead>
          <tr>
            <th>Score</th>
            {COLOR_ORDER.map((color) => (
              <th key={color}>{COLOR_LABELS[color]}</th>
            ))}
          </tr>
        </thead>
        <tbody key={tab.key}>
          { renderAnimatedRows(chart, tab) }
        </tbody>
      </table>
    </div>
  );
}

export default Table;