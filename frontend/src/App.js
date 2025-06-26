import React, { useEffect, useState } from "react";
import "./App.css";

const API_BASE = process.env.REACT_APP_API_BASE || "http://localhost:8000";

const COLOR_THEMES = ["green", "blue", "purple", "orange", "pink"];

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

const TAB_LIST = [
  { key: "abc", label: "AtCoder Beginner Contest" },
  { key: "arc", label: "AtCoder Regular Contest" },
  { key: "agc", label: "AtCoder Grand Contest" },
  { key: "profile", label: "Profile" },
];

function CardHeader({title, userName, setUserName}) {
  return (
    <div className="card-header">
      <div className="card-title">{title}</div>
      <div className="user-name-box">
        <input
          type="text"
          className="user-name-input"
          placeholder="Enter username"
          value={userName}
          onChange={(e) => setUserName(e.target.value)}
          style={{
            padding: "0.25rem 0.5rem",
            borderRadius: "4px",
            border: "1px solid #ccc",
          }}
        />
      </div>
    </div>
  );
}

function Tabs({activeTab, setActiveTab}){
  return (
    <div className="tabs">
      {TAB_LIST.map((tab) => (
        <div
          key={tab.key}
          className={`tab${activeTab === tab.key ? " active" : ""}`}
          onClick={() => setActiveTab(tab.key)}
          data-tab={`table-${tab.key}`}
        >
          {tab.label}
        </div>
      ))}
    </div>
  );
}

function Profile({ userName, profile, profileLoading, profileError }) {
  return (
    <div>
      <div style={{
        fontWeight: 700,
        fontSize: "1.25rem",
        marginBottom: "1rem",
        textAlign: "center"
      }}>
        <span role="img" aria-label="profile" style={{ marginRight: 8 }}>👤</span>
        AtCoder Profile
      </div>
      {!userName ? (
        <div style={{ color: "var(--empty-color)", textAlign: "center" }}>
          Enter a username to view profile.
        </div>
      ) : profileLoading ? (
        <div style={{ color: "var(--primary)", textAlign: "center" }}>
          Loading profile...
        </div>
      ) : profileError ? (
        <div style={{ color: "red", textAlign: "center" }}>
          {profileError}
        </div>
      ) : profile ? (
        <table style={{
          width: "100%",
          borderCollapse: "collapse",
          marginTop: "1rem"
        }}>
          <tbody>
            <tr>
              <td style={{ fontWeight: 600, padding: "0.5rem 0" }}>User ID</td>
              <td style={{ padding: "0.5rem 0" }}>{profile.user_id}</td>
            </tr>
            <tr>
              <td style={{ fontWeight: 600, padding: "0.5rem 0" }}>Accepted Count</td>
              <td style={{ padding: "0.5rem 0" }}>{profile.accepted_count}</td>
            </tr>
            <tr>
              <td style={{ fontWeight: 600, padding: "0.5rem 0" }}>AC Rank</td>
              <td style={{ padding: "0.5rem 0" }}>{profile.ac_rank}</td>
            </tr>
            <tr>
              <td style={{ fontWeight: 600, padding: "0.5rem 0" }}>Rated Point Sum</td>
              <td style={{ padding: "0.5rem 0" }}>
                {profile.rated_point_sum != null ? profile.rated_point_sum : "N/A"}
              </td>
            </tr>
            <tr>
              <td style={{ fontWeight: 600, padding: "0.5rem 0" }}>Rated Point Rank</td>
              <td style={{ padding: "0.5rem 0" }}>{profile.rated_point_sum_rank}</td>
            </tr>
          </tbody>
        </table>
      ) : null}
    </div>
  );
}

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

function renderAnimatedRows(chart, tab) {
  if (!chart || !chart[tab.key]) return null;
  return Object.entries(chart[tab.key]).map(([score, colors], rowIndex) => {
    const total = Object.values(colors).reduce((a, b) => a + b, 0);
    return (
      <tr key={score}>
        <td colSpan={COLOR_ORDER.length + 1} style={{ padding: 0, border: "none", background: "none" }}>
          <div
            className="fade-row"
            style={{
              animation: "fadeInUp 0.5s ease forwards",
              animationDelay: `${rowIndex * 0.1}s`,
              opacity: 0,
              display: "flex",
              alignItems: "center",
              height: '4.8rem',
            }}
          >
            <span className="score-label" style={{ minWidth: 60, textAlign: "center" }}>{score}</span>
            {COLOR_ORDER.map((color) => {
              const amount = colors[color] || 0;
              const percent = total ? ((amount / total) * 100).toFixed(2) : "0.00";
              return (
                <div key={color} style={{ flex: 1, textAlign: "center" }}>
                  <div className={`stats-container${amount === 0 ? " zero-amount" : ""}`}>
                    <UpperStat color={color} amount={amount} percent={percent} />
                    <Percent percent={percent} amount={amount} color={color} />
                  </div>
                </div>
              );
            })}
          </div>
        </td>
      </tr>
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
          {chart && chart[tab.key]
            ? renderAnimatedRows(chart, tab)
            : (
              <tr>
                <td colSpan={COLOR_ORDER.length + 1}>Loading...</td>
              </tr>
            )
          }
        </tbody>
      </table>
    </div>
  );
}

function UserInput({ userName, setUserName , profile, profileLoading, profileError, setProfile, setProfileLoading, setProfileError }) {
  // Fetch profile when userName changes
  useEffect(() => {
    if (!userName) {
      setProfile(null);
      setProfileError(null);
      return;
    }
    setProfileLoading(true);
    setProfileError(null);

    const handler = setTimeout(() => {
      fetch(`${API_BASE}/profile/${encodeURIComponent(userName)}`)
        .then((res) => {
          if (!res.ok) throw new Error("Profile not found");
          return res.json();
        })
        .then((data) => {
          setProfile(data);
          setProfileLoading(false);
        })
        .catch((err) => {
          setProfile(null);
          setProfileError(err.message);
          setProfileLoading(false);
        });
    }, 500); // 500ms debounce

    return () => clearTimeout(handler);
  }, [userName, setProfile, setProfileError, setProfileLoading]);
  
  return(
    <div className='user-input-outer'>
      <div className="user-input-inner">
        <Profile
          userName={userName}
          profile={profile}
          profileLoading={profileLoading}
          profileError={profileError}
        />
      </div>
    </div>
  );
}

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

function Body({
  activeTab, setActiveTab, userName, setUserName,
  profile, setProfile, profileLoading, setProfileLoading, profileError, setProfileError
}) {
  const [chart, setChart] = useState(null);

  useEffect(() => {
    fetch(`${API_BASE}/json/chart.json`)
      .then((res) => res.json())
      .then((data) => setChart(data));
  }, []);

  return(
    <div className="container">
      <div className="card">
        <CardHeader title="AtCoder Problems" userName={userName} setUserName={setUserName} />
        <Tabs activeTab={activeTab} setActiveTab={setActiveTab}/>
          <div className="tables">
            {activeTab === "profile" ? (
              <UserInput
                userName={userName}
                setUserName={setUserName}
                profile={profile}
                profileLoading={profileLoading}
                profileError={profileError}
                setProfile={setProfile}
                setProfileLoading={setProfileLoading}
                setProfileError={setProfileError}
              />
            ) : (
              <Table
                tab={TAB_LIST.find(tab => tab.key === activeTab)}
                chart={chart}
              />
            )}
          </div>
      </div>
    </div>
  );
}

function WebsiteButton() {
  return(
    <div
      className="floating-button"
      onClick={() =>
        window.open("https://kenkoooo.com/atcoder/#/table", "_blank")
      }
      title="Open AtCoder Problems Table"
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
  );
}

function ThemeToggleButton() {
  const toggleTheme = () => {
    const root = document.documentElement;
    const mode = root.getAttribute("data-mode") === "dark" ? "light" : "dark";
    root.setAttribute("data-mode", mode);
    localStorage.setItem("theme-mode", mode);
  };
  return (
    <div className="theme-toggle" onClick={toggleTheme} title="Toggle Theme">
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
  );
}

function CycleThemeButton() {
  const cycleThemeColor = () => {
    const root = document.documentElement;
    const current = root.getAttribute("data-color") || "green";
    const idx = COLOR_THEMES.indexOf(current);
    const next = COLOR_THEMES[(idx + 1) % COLOR_THEMES.length];
    root.setAttribute("data-color", next);
    localStorage.setItem("theme-color", next);
  };
  return(
    <div
      className="color-theme-toggle"
      onClick={cycleThemeColor}
      title="Cycle Theme Color"
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
          d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01"
        ></path>
      </svg>
    </div>
  );
}

function Buttons() {
  // Theme and color toggling
  useEffect(() => {
    const savedMode = localStorage.getItem("theme-mode");
    const savedColor = localStorage.getItem("theme-color");
    if (savedMode) {
      document.documentElement.setAttribute("data-mode", savedMode);
    } else if (!document.documentElement.getAttribute("data-mode")) {
      document.documentElement.setAttribute("data-mode", "light");
    }
    if (savedColor) {
      document.documentElement.setAttribute("data-color", savedColor);
    } else if (!document.documentElement.getAttribute("data-color")) {
      document.documentElement.setAttribute("data-color", "green");
    }
  }, []);
  return (
    <div className="floating-buttons">
      <WebsiteButton />
      <ThemeToggleButton />
      <CycleThemeButton />
    </div>
  );
}

function App() {
  const [userName, setUserName] = useState("")
  const [activeTab, setActiveTab] = useState("abc");
  const [profile, setProfile] = useState(null);
  const [profileLoading, setProfileLoading] = useState(false);
  const [profileError, setProfileError] = useState(null); 

  return (
    <>
      <Header activeTab={activeTab}/>

      <Body 
        activeTab={activeTab}
        setActiveTab={setActiveTab}
        userName={userName}
        setUserName={setUserName}
        profile={profile}
        setProfile={setProfile}
        profileLoading={profileLoading}
        setProfileLoading={setProfileLoading}
        profileError={profileError}
        setProfileError={setProfileError}
      />

      <Buttons/>
    </>
  );
}

export default App;
