import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './pages/Home';
import Business from './pages/Business';
import Political from './pages/Political';
import Sports from './pages/Sports';
import Technology from './pages/Technology';
import Entertainment from './pages/Entertainment';
import Chat from './pages/Chat';
function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/business" element={<Business />} />
        <Route path="/political" element={<Political />} />
        <Route path="/sports" element={<Sports />} />
        <Route path="/technology" element={<Technology />} />
        <Route path="/entertainment" element={<Entertainment />} />
        <Route path="/chat" element={<Chat />} />

      </Routes>
      <Footer />
    </Router>
  );
}

export default App;
