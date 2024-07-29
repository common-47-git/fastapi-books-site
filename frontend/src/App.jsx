import './App.css';
import axios from "axios";
import { useEffect, useState } from "react";
import BookInfo from './components/BookInfo';

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
    <div className="books-grid">
      {books.length > 0 ? 
        books.map((book, index) => (
          <BookInfo key={index} book={book} />
        )) 
        : "Loading..."
      }
    </div>
  );
}

export default App;

