// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LandingPage from './components/LandingPage';
import HostLoginPage from './components/HostLoginPage';
import QuizPage from './components/QuizPage';
import ParticipantQuizPage from './components/ParticipantQuizPage';

function App() {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/host" element={<HostLoginPage />} />
          <Route path="/quiz" element={<QuizPage />} />
          <Route path="/participant" element={<ParticipantQuizPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
