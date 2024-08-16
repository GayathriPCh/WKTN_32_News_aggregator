import { Link } from 'react-router-dom';
import './Header.css'; // Import the CSS file for styles

function Header() {
  return (
    <header className="header">
      <h1 className="title">Buzzlines</h1>
      <nav className="nav">
        <Link to="/" className="nav-link home-link">Home</Link>
        <Link to="/business" className="nav-link business-link">Business</Link>
        <Link to="/political" className="nav-link political-link">Political</Link>
        <Link to="/sports" className="nav-link sports-link">Sports</Link>
        <Link to="/technology" className="nav-link technology-link">Technology</Link>
        <Link to="/entertainment" className="nav-link entertainment-link">Entertainment</Link>
        <Link to="/chat" className="nav-link chat-link">
          <button className="ai-chat-button">AI Chat</button>
        </Link>
      </nav>
    </header>
  );
}

export default Header;
