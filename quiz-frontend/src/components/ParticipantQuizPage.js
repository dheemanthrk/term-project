// src/components/ParticipantQuizPage.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ParticipantQuizPage() {
  const [quizQuestions, setQuizQuestions] = useState([]);
  const [answers, setAnswers] = useState([]);

  useEffect(() => {
    // Fetch quiz questions using the Retrieve Quiz Set API
    const fetchQuizQuestions = async () => {
      try {
        const response = await axios.get('/retrievequizset');
        setQuizQuestions(response.data.questions);
      } catch (error) {
        console.error('Error fetching quiz questions:', error);
      }
    };
    fetchQuizQuestions();
  }, []);

  const handleAnswerChange = (event, index) => {
    const newAnswers = [...answers];
    newAnswers[index] = event.target.value;
    setAnswers(newAnswers);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      // Submit answers using the Submit Answers API
      await axios.post('/submitanswers', { answers });
      alert('Answers submitted successfully!');
    } catch (error) {
      console.error('Error submitting answers:', error);
      alert('Failed to submit answers. Please try again.');
    }
  };

  return (
    <div>
      <h2>Participant Quiz Page</h2>
      <form onSubmit={handleSubmit}>
        {quizQuestions.map((question, index) => (
          <div key={question.questionid}>
            <h3>Question {index + 1}</h3>
            <p>{question.questiontext}</p>
            {question.options.map((option, optionIndex) => (
              <label key={optionIndex}>
                <input
                  type="radio"
                  name={`question_${index}`}
                  value={option}
                  onChange={(event) => handleAnswerChange(event, index)}
                />
                {option}
              </label>
            ))}
          </div>
        ))}
        <button type="submit">Submit Answers</button>
      </form>
    </div>
  );
}

export default ParticipantQuizPage;
