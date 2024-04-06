// src/components/QuizPage.js
import React from 'react';
import { Link } from 'react-router-dom';

function QuizPage() {
  return (
    <div>
      <h2>Quiz Page</h2>
      <div>
        <Link to="/retrievequizset">
          <button>View Quiz Questions</button>
        </Link>
        <Link to="/updatequestion">
          <button>Update Question</button>
        </Link>
        <Link to="/deletequestion">
          <button>Delete Question</button>
        </Link>
        <Link to="/createquizset">
          <button>Create Quiz Set</button>
        </Link>
      </div>
    </div>
  );
}

export default QuizPage;
