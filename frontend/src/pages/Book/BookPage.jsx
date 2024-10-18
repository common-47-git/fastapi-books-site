import { useEffect, useState } from "react";
import axios from "axios";
import { useParams, useSearchParams, Link } from "react-router-dom";

import Header from '../../components/Header/Header';
import Footer from '../../components/Footer/Footer';
import DefaultButton from '../../components/DefaultButton/DefaultButton';
import './css/styles.css';

function BookPage() {
  const { bookName } = useParams();
  const [book, setBook] = useState(null);
  const [authors, setAuthors] = useState([]); // State to hold authors
  const [searchParams] = useSearchParams();
  const volume = searchParams.get('volume') || 1;
  const chapter = searchParams.get('chapter') || 1;

  // Fetch book details
  useEffect(() => {
    const fetchBook = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/books/${bookName}`);
        setBook(response.data);
      } catch (error) {
        console.error("Error fetching book:", error);
      }
    };

    fetchBook();
  }, [bookName]);

  // Fetch authors
  useEffect(() => {
    const fetchAuthors = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/books/${bookName}/authors`);
        setAuthors(response.data);
      } catch (error) {
        console.error("Error fetching authors:", error);
      }
    };

    fetchAuthors();
  }, [bookName]);

  if (!book) {
    return <div>Loading...</div>;
  }

  // Format author names
  const authorNames = authors.map(author => `${author.author_name} ${author.author_surname}`).join(', ');

  return (
    <>
      <Header />
      <main className="main">
        <div className="container">
          <div className="book-detail">
            <div className="book-nav">
              <div className="book-cover">
                <img className="book-cover-img" src={book.book_cover} alt={`${book.book_name} cover`} />
              </div>
              <Link to={{
                pathname: `/books/${bookName}/read`,
                search: `?volume=${volume}&chapter=${chapter}`,
              }}>
                <DefaultButton content={"READ"} />
              </Link>
            </div>

            <div className="book-detail-container">
              <h1>{book.book_name}</h1>
              <div className="book-detail-row"><strong>Author:</strong> {authorNames || "Unknown"}</div>
              <div className="book-detail-row"><strong>Country:</strong> {book.book_country}</div>
              <div className="book-detail-row"><strong>Release Date:</strong> {new Date(book.book_release_date).toLocaleDateString()}</div>
              <div className="book-detail-row"><strong>Description:</strong> {book.book_description || "No description available"}</div>
            </div>
          </div>
        </div>
      </main>
      <Footer />
    </>
  );
}

export default BookPage;
