import { useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import '../App.css';

import Header from '../components/Header';

function Books() {
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
    <> 
      <Header />
      <div className="books-grid">
        {books.length > 0 ? 
          books.map((book, index) => (
            <Link to={`/books/${book.book_name}`} key={index} className="book-container">
              <div className="book-title">{book.book_name}</div>
              <div className="book-detail"><strong>Country:</strong> {book.book_country}</div>
              <div className="book-detail"><strong>Release Date:</strong> {new Date(book.book_release_date).toLocaleDateString()}</div>
              <div className="book-description">{book.book_description || "No description available"}</div>
            </Link>
          )) 
          : "Loading..."
        }
      </div>
    </>
  );
}

export default Books;
