import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Home from './pages/Home/Home';
import Stats from './pages/Stats/Stats';
import { BookProvider } from './context/BookContext';

const App = () => {
  return (
    <BookProvider>
      <Router>
        <nav>
          <Link to="/">Home</Link> | <Link to="/stats">Stats</Link>
        </nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/stats" element={<Stats />} />
        </Routes>
      </Router>
    </BookProvider>
  );
};

export default App;
