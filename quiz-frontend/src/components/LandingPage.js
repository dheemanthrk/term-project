// src/components/LandingPage.js
import React from 'react';
import { Link } from 'react-router-dom';

function LandingPage() {
  return (
    <div>
      <h2>Welcome to Quiz App</h2>
      <div>
        <Link to="/host">
          <button>Host</button>
        </Link>
        <Link to="/participant">
          <button>Participant</button>
        </Link>
      </div>
    </div>
  );
}

export default LandingPage;
