import "./BookInfo.css"; // Import the CSS file

function BookInfo({ book }) {
  return (
    <div>
      <div className="book-container">
        <div className="book-title">{book.book_name}</div>
        <div className="book-detail"><strong>Country:</strong> {book.book_country}</div>
        <div className="book-detail"><strong>Release Date:</strong> {new Date(book.book_release_date).toLocaleDateString()}</div>
        <div className="book-description"><strong>Description:</strong> {book.book_description || "No description available"}</div>
      </div>
    </div>
  );
}

export default BookInfo;
