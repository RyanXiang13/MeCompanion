import React from "react";

const ResponseDisplay = ({ sentiment, response }) => {
  return (
    <div>
      {sentiment && (
        <div>
          <h2>Sentiment Analysis</h2>
          <p>Polarity: {sentiment.polarity}</p>
          <p>Subjectivity: {sentiment.subjectivity}</p>
        </div>
      )}
      {response && (
        <div>
          <h2>AI Response</h2>
          <p>{response}</p>
        </div>
      )}
    </div>
  );
};

export default ResponseDisplay;