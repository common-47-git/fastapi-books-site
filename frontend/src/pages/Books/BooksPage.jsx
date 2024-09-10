import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";


import Header from '../../components/Header/Header';
import Footer from '../../components/Footer/Footer';
import './css/styles.css'

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
      <main className="main">
        <div className="container">
          <div className="books-grid">
            {books.length > 0 ? 
              books.map((book, index) => (
                <Link to={`/books/${book.book_name}`} key={index} className="book-container">
                  <div className="book-cover">
                    <img className="book-cover-img" src={book.book_cover} alt={`${book.book_name} cover`} />
                  </div>
                  <div className="book-title">{book.book_name}</div>
                </Link>
              )) 
              : "Loading..."
            }
          </div>
        </div>
      </main>
      <Footer></Footer>
    </>
  );
}

export default Books;
