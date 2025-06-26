import React, { useEffect } from "react";
import { useState } from "react";

const API_BASE = process.env.REACT_APP_API_BASE || "http://localhost:8000";

function Header({activeTab}) {
  const [latest, setLatest] = useState(null);

  useEffect(() => {
    fetch(`${API_BASE}/json/latest.json`)
      .then((res) => res.json())
      .then((data) => setLatest(data));
  }, []);

  return(
    <header>
        <div className="header-bg">
          <div className="header-bg-circle circle-1"></div>
          <div className="header-bg-circle circle-2"></div>
        </div>
        <div className="container header-content">
          <h1>AtCoder Statistics</h1>
          {latest &&
            latest[activeTab] &&
            latest[activeTab] !== "N/A" &&
            latest[activeTab] !== "-" && (
              <h2
                key={activeTab + latest[activeTab]}
                id="latest-contest-label"
                data-latest-abc={latest.abc}
                data-latest-arc={latest.arc}
                data-latest-agc={latest.agc}
                aria-live="polite"
                style={{
                  fontSize: "1.25rem",
                  fontWeight: 500,
                  opacity: 0,
                  animation: "fadeInUp 0.8s ease-out 0.3s",
                  animationFillMode: "forwards",
                  minHeight: "1.7em",
                }}
              >
                Latest Contest: {latest[activeTab]}
              </h2>
            )}
          {(!latest ||
            !latest[activeTab] ||
            latest[activeTab] === "N/A" ||
            latest[activeTab] === "-") && (
            <h2
              style={{
                fontSize: "1.25rem",
                fontWeight: 500,
                minHeight: "1.7em",
                visibility: "hidden",
              }}
            >
              &nbsp;
            </h2>
          )}
        </div>
      </header>
  );
}

export default Header;