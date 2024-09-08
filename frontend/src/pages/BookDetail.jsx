import '../App.css';
import { useEffect, useState } from "react";
import axios from "axios";
import { useParams, Link } from "react-router-dom";

import Header from '../components/Header';

function BookDetail() {
  const { bookName } = useParams();
  const [book, setBook] = useState(null);
  const [author, setAuthor] = useState(null);

  useEffect(() => {
    axios.get(`http://127.0.0.1:8000/books/${bookName}`)
      .then(response => {
        setBook(response.data);
      })
      .catch(error => {
        console.error("Error fetching book:", error);
      });

    axios.get(`http://127.0.0.1:8000/books/${bookName}/author`)
      .then(response => {
        setAuthor(response.data);
      })
      .catch(error => {
        console.error("Error fetching author:", error);
      });
  }, [bookName]);

  if (!book || !author) {
    return <div>Loading...</div>;
  }

  return (
    <>
      <Header></Header>
      <main className="main">
        <div className="main-book-detail">
          <div className="book-detail-container">
            <h1>{book.book_name}</h1>
            <div><strong>Author:</strong> {author.author_name} {author.author_surname}</div>
            <div><strong>Country:</strong> {book.book_country}</div>
            <div><strong>Release Date:</strong> {new Date(book.book_release_date).toLocaleDateString()}</div>
            <div><strong>Description:</strong> {book.book_description || "No description available"}</div>
          </div>
          <Link to={`/books/${bookName}/read`} className="read-chapter-link" >
            Read
          </Link>
        </div>
      </main>
    </>
  );
}

export default BookDetail;
