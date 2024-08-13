import ChatComponent from '../components/ChatComponent';
import './Chat.css'; // Import CSS for custom styling

function Chat() {
  return (
    <div className="chat-container">
      <h1>AI Chat</h1>
      <ChatComponent />
    </div>
  );
}

export default Chat;
