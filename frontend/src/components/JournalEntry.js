import React, { useState } from "react";
import { analyzeText } from "../api";

const JournalEntry = ({ token }) => {
  const [inputText, setInputText] = useState("");
  const [response, setResponse] = useState("");
  const [sentiment, setSentiment] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await analyzeText(inputText, token);
    if (data.error) {
      alert(data.error);
    } else {
      setSentiment(data.sentiment);
      setResponse(data.response);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <textarea
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          placeholder="How are you feeling today?"
          rows="5"
          cols="50"
        />
        <br />
        <button type="submit">Get Support</button>
      </form>
    </div>
  );
};

export default JournalEntry;