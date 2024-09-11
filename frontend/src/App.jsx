import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import HomePage from './pages/Home/HomePage';
import BooksPage from './pages/Books/BooksPage';
import BookPage from './pages/Book/BookPage'; 
import BookReadPage from './pages/BookRead/BookReadPage'; 
import UserLogin from './pages/UserLogin/UserLogin'; 
import NotFoundPage from './pages/NotFound/NotFoundPage'; 

function App() {
  
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/books" element={<BooksPage />} />
        <Route path="/books/:bookName" element={<BookPage />} />
        <Route path="/books/:bookName/read" element={<BookReadPage />} />
        <Route path="/users/login" element={<UserLogin />} />
        <Route path="*" element={<NotFoundPage />} />
      </Routes>
    </Router>
  );
  
}

export default App;
