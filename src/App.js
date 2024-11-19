import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      alert("Please upload a file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(
        "https://engagesense.onrender.com/analyze",
        formData
      );
      setResult(response.data);
    } catch (error) {
      console.error("Error uploading file:", error);
      alert("An error occurred while uploading the file.");
    }
  };

  return (
    <div className="App">
      <h1>EngageSense File Analysis</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="file">Choose a file to analyze:</label>
        <input type="file" id="file" onChange={handleFileChange} />
        <button type="submit">Analyze</button>
      </form>

      {result && (
        <div className="result">
          <h2>Analysis Results:</h2>
          <p><strong>Emotional:</strong> {result.emotional}</p>
          <p><strong>Mental:</strong> {result.mental}</p>
          <p><strong>Physical:</strong> {result.physical}</p>
          <p><strong>Spiritual:</strong> {result.spiritual}</p>
          <p><strong>Word Count:</strong> {result.word_count}</p>
          <p><strong>Character Count:</strong> {result.char_count}</p>
        </div>
      )}
    </div>
  );
}

export default App;
