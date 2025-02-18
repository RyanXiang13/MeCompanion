import React, { useState } from "react";
import Navbar from "./components/Navbar";
import JournalEntry from "./components/JournalEntry";
import ResponseDisplay from "./components/ResponseDisplay";
import { login, register } from "./api";
import "./App.css";

function App() {
  const [token, setToken] = useState("");
  const [sentiment, setSentiment] = useState(null);
  const [response, setResponse] = useState("");

  const handleLogin = async (username, password) => {
    const data = await login(username, password);
    if (data.access_token) {
      setToken(data.access_token);
    }
  };

  const handleRegister = async (username, password) => {
    const data = await register(username, password);
    if (data.message) {
      alert(data.message);
    }
  };

  return (
    <div className="App">
      <Navbar />
      <JournalEntry token={token} />
      <ResponseDisplay sentiment={sentiment} response={response} />
    </div>
  );
}

export default App;