import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";


import Header from '../../components/Header/Header';
import Footer from '../../components/Footer/Footer';

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
            </Link>
          )) 
          : "Loading..."
        }
      </div>
      <Footer></Footer>
    </>
  );
}

export default Books;
