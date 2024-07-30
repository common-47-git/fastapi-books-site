import './App.css';
import axios from "axios";
import { useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import RawBook from './components/RawBook';
import BookDetail from './components/BookDetail'; // Import the BookDetail component

function App() {
  const [books, setBooks] = useState([]);

  const fetchBooks = () => {
    axios.get("http://127.0.0.1:8000/books")
      .then(response => {
        setBooks(response.data);
      })
      .catch(error => {
        console.error("Error fetching books:", error);
      });
  };

  useEffect(() => {
    fetchBooks();
  }, []);

  return (
    <Router>
      <Routes>
        <Route path="/" element={
          <div className="books-grid">
            {books.length > 0 ? 
              books.map((book, index) => (
                <RawBook key={index} book={book} />
              )) 
              : "Loading..."
            }
          </div>
        } />
        <Route path="/books/:bookName" element={<BookDetail />} />
      </Routes>
    </Router>
  );
}

export default App;
