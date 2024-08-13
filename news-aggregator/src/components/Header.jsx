import { Link } from 'react-router-dom';

function Header() {
  return (
    <header>
      <h1>News App</h1>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/business">Business</Link>
        <Link to="/political">Political</Link>
        <Link to="/sports">Sports</Link>
        <Link to="/technology">Technology</Link>
        <Link to="/entertainment">Entertainment</Link>
      </nav>
    </header>
  );
}

export default Header;
