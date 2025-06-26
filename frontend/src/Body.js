import React, { useState, useEffect } from "react";
import Table from "./Table";

const API_BASE = process.env.REACT_APP_API_BASE || "http://localhost:8000";

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