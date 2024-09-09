import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import HomePage from './pages/Home/HomePage';
import BooksPage from './pages/Books/BooksPage';
import BookPage from './pages/Book/BookPage'; 
import BookReadPage from './pages/BookRead/BookReadPage'; 

function App() {
  
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/books" element={<BooksPage />} />
        <Route path="/books/:bookName" element={<BookPage />} />
        <Route path="/books/:bookName/read" element={<BookReadPage />} />
      </Routes>
    </Router>
  );
  
}

export default App;
