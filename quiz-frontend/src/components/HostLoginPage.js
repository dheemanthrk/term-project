// src/components/HostLoginPage.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function HostLoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate(); // Update the import and hook

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // Hardcoded login credentials
    const hardcodedUsername = 'admin';
    const hardcodedPassword = 'password';
    if (username === hardcodedUsername && password === hardcodedPassword) {
      // Redirect to Quiz Page upon successful login
      navigate('/quiz'); // Update history.push() to navigate()
    } else {
      alert('Invalid username or password');
    }
  };

  return (
    <div>
      <h2>Host Login</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Username:
          <input type="text" value={username} onChange={handleUsernameChange} />
        </label>
        <label>
          Password:
          <input type="password" value={password} onChange={handlePasswordChange} />
        </label>
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default HostLoginPage;
