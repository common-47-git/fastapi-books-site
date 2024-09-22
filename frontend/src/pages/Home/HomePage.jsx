import { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom'; 
import Footer from '../../components/Footer/Footer';
import Header from '../../components/Header/Header';
import BookPreview from '../../components/BookPreview/BookPreview';
import './css/styles.css';

function HomePage() {
  const [books, setBooks] = useState([]);

  const fetchBooks = () => {
    axios.get("http://127.0.0.1:8000/books/all")
      .then(response => {
        // Sort books by release date and get the first 5
        const sortedBooks = response.data.sort((a, b) => 
          new Date(b.book_release_date) - new Date(a.book_release_date)
        ).slice(0, 5); // Get first 5 books
        setBooks(sortedBooks);
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
          <div className="books-recently">
            <h2>Recently Added Books</h2>
            <div className="books-grid">
              {books.length > 0 ? 
                books.map((book, index) => (
                  <Link to={`/books/${book.book_name}`} key={index} className="book-container">
                    <BookPreview book={book} />
                  </Link>
                )) 
                : "Loading..."
              }
            </div>
          </div>
        </div>
      </main>
      <Footer />
    </>
  );
}

export default HomePage;
