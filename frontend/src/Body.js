import React, { useState, useEffect } from "react";

const API_BASE = process.env.REACT_APP_API_BASE || "http://localhost:8000";

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
    <div className="profile-container">
      <div className="profile-title">
        <span role="img" aria-label="profile" className="profile-emoji">👤</span>
        AtCoder Profile
      </div>
      {!userName ? (
        <div className="profile-empty">Enter a username to view profile.</div>
      ) : profileLoading ? (
        <div className="profile-loading">Loading profile...</div>
      ) : profileError ? (
        <div className="profile-error">{profileError}</div>
      ) : profile ? (
        <table className="profile-table">
          <tbody>
            <tr>
              <td className="profile-label">User ID</td>
              <td className="profile-value">{profile.user_id}</td>
            </tr>
            <tr>
              <td className="profile-label">Accepted Count</td>
              <td className="profile-value">{profile.accepted_count}</td>
            </tr>
            <tr>
              <td className="profile-label">AC Rank</td>
              <td className="profile-value">{profile.ac_rank}</td>
            </tr>
            <tr>
              <td className="profile-label">Rated Point Sum</td>
              <td className="profile-value">
                {profile.rated_point_sum != null ? profile.rated_point_sum : "N/A"}
              </td>
            </tr>
            <tr>
              <td className="profile-label">Rated Point Rank</td>
              <td className="profile-value">{profile.rated_point_sum_rank}</td>
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

function UserInput({ userName, profileState }) {
  const { profile, setProfile, profileLoading, setProfileLoading, profileError, setProfileError } = profileState;
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

function Body({
  activeTab, setActiveTab, userName, setUserName,profileState
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
                profileState={profileState}
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

export default Body;