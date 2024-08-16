import { useState } from 'react';
import { getGroqChatCompletion } from '../api/aiChat';
import './ChatComponent.css';
import mascot from './mascot.png'; // Adjust the path based on where you store the image

function ChatComponent() {
  const [prompt, setPrompt] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    const chatCompletion = await getGroqChatCompletion(prompt);
    setResponse(chatCompletion.choices[0]?.message?.content || "No response");
  };

  const handleReload = () => {
    window.location.reload();
  };

  return (
    <div className="chat-component">
      <h2 className="chat-title">Buzz - Your Personal News Discussing Buddy</h2>
      <form onSubmit={handleSubmit}>
        <textarea
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Enter your prompt here"
          rows="4"
          cols="50"
          className="chat-textarea"
        />
        <button type="submit" className="chat-submit-button">Submit</button>
      </form>
      <div className="chat-response">
        <div className="chat-response-header">
          <img src={mascot} alt="AI Buddy" className="chat-pfp" />
          <h3>Response:</h3>
        </div>
        <p>{response}</p>
      </div>
      <button onClick={handleReload} className="chat-reload-button">Talk More</button>
    </div>
  );
}

export default ChatComponent;
