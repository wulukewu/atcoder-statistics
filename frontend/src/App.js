import React, { useState } from "react";
import "./App.css";
import Buttons from "./Buttons";
import Header from "./Header";
import Body from "./Body";

function App() {
  const [userName, setUserName] = useState("")
  const [activeTab, setActiveTab] = useState("abc");
  const [profile, setProfile] = useState(null);
  const [profileLoading, setProfileLoading] = useState(false);
  const [profileError, setProfileError] = useState(null);
  const profileState = {
    profile,
    setProfile,
    profileLoading,
    setProfileLoading,
    profileError,
    setProfileError,
  };

  return (
    <>
      <Header activeTab={activeTab}/>

      <Body 
        activeTab={activeTab}
        setActiveTab={setActiveTab}
        userName={userName}
        setUserName={setUserName}
        profileState={profileState}
      />

      <Buttons/>
    </>
  );
}

export default App;
