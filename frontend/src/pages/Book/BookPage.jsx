import { useEffect, useState } from "react";
import axios from "axios";
import { useParams, useSearchParams, Link } from "react-router-dom";

import Header from '../../components/Header/Header';
import Footer from '../../components/Footer/Footer';
import DefaultButton from '../../components/DefaultButton/DefaultButton';
import DefaultDropdownList from '../../components/DefaultDropdownList/DefaultDropdownList';
import './css/styles.css';

function BookPage() {
  const { bookName } = useParams();
  const [bookInfo, setBookInfo] = useState(null);
  const [searchParams] = useSearchParams();
  const volume = searchParams.get('volume') || 1;
  const chapter = searchParams.get('chapter') || 1;

  const [shelf, setShelf] = useState("put on the shelf"); // Default shelf to "put on the shelf"
  const [message, setMessage] = useState(null); // Status message

  const listOfOptions = ['put on the shelf', 'reading', 'completed', 'in plans'];

  // Fetch book information with authentication
  useEffect(() => {
    const fetchBookInfo = async () => {
      const token = localStorage.getItem('accessToken');
  
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/books/${bookName}`,
          {
            headers: {
              Authorization: `Bearer ${token}`, // Include authorization header
            },
          }
        );
        setBookInfo(response.data);
  
        // Normalize shelf to lowercase and default to 'reading' if not found
        const shelfFromAPI = response.data.book_shelf?.toLowerCase() || "put on the shelf";
        setShelf(listOfOptions.includes(shelfFromAPI) ? shelfFromAPI : "put on the shelf");
      } catch (error) {
        console.error("Error fetching book info:", error);
        setMessage("Failed to fetch book information.");
      }
    };
  
    fetchBookInfo();
  }, [bookName]);
  

  // Handle dropdown changes
  const handleShelfChange = async (event) => {
    const newShelf = event.target.value;
    setShelf(newShelf);

    await handleAddToLibrary(newShelf);
  };

  // Add book to the library
  const handleAddToLibrary = async (shelfToPut) => {
    const token = localStorage.getItem('accessToken');

    if (!token) {
      setMessage("User is not authenticated. Please log in.");
      return;
    }

    try {
      await axios.post(
        `http://127.0.0.1:8000/users/bookmark?book_name=${bookName}&shelf=${shelfToPut}`,
        null,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      setMessage("Book added successfully!");
    } catch (error) {
      console.error("API Error:", error.response?.data || error.message);
      setMessage("Failed to add the book to your library.");
    }
  };

  if (!bookInfo) {
    return <div>Loading...</div>;
  }

  const { book, book_tags: bookTags, book_authors: bookAuthors } = bookInfo;

  const authorNames = bookAuthors.map(author => `${author.author_name} ${author.author_surname}`).join(', ');
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
              <Link
                to={{
                  pathname: `/books/${bookName}/read`,
                  search: `?volume=${volume}&chapter=${chapter}`,
                }}
              >
                <DefaultButton content="READ" />
              </Link>
              <div className="dropdown-add-list">
                <DefaultDropdownList
                  listOfOptions={listOfOptions}
                  shelf={shelf} // Pass the shelf prop directly
                  handleShelfChange={handleShelfChange} // Handle shelf change
                />
              </div>
            </div>

            <div className="book-detail-container">
              <h1>{book.book_name}</h1>
              <div className="book-detail-row"><strong>Author:</strong> {authorNames || "Unknown"}</div>
              <div className="book-detail-row"><strong>Country:</strong> {book.book_country}</div>
              <div className="book-detail-row"><strong>Release Date:</strong> {new Date(book.book_release_date).toLocaleDateString()}</div>
              <div className="book-detail-row"><strong>Tags:</strong> {tagNames || "No tags available"}</div>
              <div className="book-detail-row"><strong>Description:</strong> {book.book_description || "No description available"}</div>
            </div>

            {message && <div className="status-message">{message}</div>}
          </div>
        </div>
      </main>
      <Footer />
    </>
  );
}

export default BookPage;
