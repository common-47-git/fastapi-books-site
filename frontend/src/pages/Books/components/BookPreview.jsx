import React from "react";
import '../css/styles.css';

function BookPreview({ book }) {
  return (
    <>
      <div className="book-cover">
        <img className="book-cover-img" src={book.book_cover} alt={`${book.book_name} cover`} />
      </div>
      <div className="book-title">{book.book_name}</div>
    </>
  );
}

export default BookPreview;
