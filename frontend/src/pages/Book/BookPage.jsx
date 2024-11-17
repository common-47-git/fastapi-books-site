import { useEffect, useState } from "react";
import axios from "axios";
import { useParams, useSearchParams, Link } from "react-router-dom";

import Header from '../../components/Header/Header';
import Footer from '../../components/Footer/Footer';
import DefaultButton from '../../components/DefaultButton/DefaultButton';
import './css/styles.css';

function BookPage() {
  const { bookName } = useParams();
  const [bookInfo, setBookInfo] = useState(null); // Combined state for book info
  const [searchParams] = useSearchParams();
  const volume = searchParams.get('volume') || 1;
  const chapter = searchParams.get('chapter') || 1;

  // Fetch all book information (book, authors, tags)
  useEffect(() => {
    const fetchBookInfo = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/books/${bookName}`);
        setBookInfo(response.data);
      } catch (error) {
        console.error("Error fetching book info:", error);
      }
    };

    fetchBookInfo();
  }, [bookName]);

  if (!bookInfo) {
    return <div>Loading...</div>;
  }

  const { book, book_tags: bookTags, book_authors: bookAuthors } = bookInfo;

  // Format author names
  const authorNames = bookAuthors.map(author => `${author.author_name} ${author.author_surname}`).join(', ');

  // Format tags
  const tagNames = bookTags.map(tag => tag.tag_name).join(', ');

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
              <div className="book-detail-row"><strong>Tags:</strong> {tagNames || "No tags available"}</div>
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
