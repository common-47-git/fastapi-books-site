import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Index from './pages/Index';
import Books from './pages/Books';
import BookDetail from './pages/BookDetail'; 
import ChapterDetail from './pages/Chapter'; 

function App() {
  

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Index />} />
        <Route path="/books" element={<Books />} />
        <Route path="/books/:bookName" element={<BookDetail />} />
        <Route path="/books/:bookName/read" element={<ChapterDetail />} />
      </Routes>
    </Router>
  );
}

export default App;
