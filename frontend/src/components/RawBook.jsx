import { Link } from "react-router-dom";
import '../App.css';

function RawBook({ book }) {
  return (
    <div>
      <Link to={`/books/${book.book_name}`} className="book-container">
        <div className="book-title">{book.book_name}</div>
        <div className="book-detail"><strong>Country:</strong> {book.book_country}</div>
        <div className="book-detail"><strong>Release Date:</strong> {new Date(book.book_release_date).toLocaleDateString()}</div>
        <div className="book-description"><strong>Description:</strong> {book.book_description || "No description available"}</div>
      </Link>
    </div>
  );
}

export default RawBook;

