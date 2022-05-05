import React from "react";
import PersonalDetails from "./profile-page/PersonalDetails";
import "./Resume.css";

function Resume() {
  return (
    <div>
      <div className="header">
        <div className="logo">Logo</div>
        <div className="dashboard">Dashboard</div>
      </div>
      <PersonalDetails/>
    </div>
  );
}

export default Resume;
