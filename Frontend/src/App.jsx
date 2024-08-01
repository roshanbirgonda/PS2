import React, { useState } from "react";
import axios from "axios";

function App() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("http://localhost:5000/predict", { input });
      setResponse(res.data);
    } catch (error) {
      console.error("Error sending input to server:", error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Text Prediction App</h1>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Enter your text"
          />
          <button type="submit">Submit</button>
        </form>
        {response && (
          <div>
            <h2>Prediction:</h2>
            <p>{JSON.stringify(response)}</p>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
