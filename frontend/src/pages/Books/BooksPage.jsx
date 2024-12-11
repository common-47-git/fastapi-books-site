import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

import Header from '../../components/Header/Header';
import Footer from '../../components/Footer/Footer';
import BookPreview from '../../components/BookPreview/BookPreview';
import './css/styles.css';

function BooksPage() {
  const [books, setBooks] = useState([]);

  const fetchBooks = () => {
    axios.get("http://127.0.0.1:8000/books/all")
      .then(response => {
        setBooks(response.data);
      })
      .catch(error => {
        console.error("Error fetching books:", error);
      });
  };

  useEffect(() => {
    fetchBooks();
  }, []); // Fetch books once when the component is mounted

  return (
    <> 
      <Header />
      <main className="main">
        <div className="container">
          <div className="books-grid">
            {books.length > 0 ?
              books.map((book, index) => (
                <Link to={`/books/${book.book_name}`} key={index} className="book-container">
                  <BookPreview book={book} />
                </Link>
              ))
              : <p>Loading...</p>
            }
          </div>
        </div>
      </main>
      <Footer />
    </>
  );
}

export default BooksPage;
