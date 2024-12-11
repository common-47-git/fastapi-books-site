import { useEffect, useState } from 'react';
import { useSearchParams, Link } from 'react-router-dom';
import Footer from '../../components/Footer/Footer';
import Header from '../../components/Header/Header';
import BookPreview from '../../components/BookPreview/BookPreview'; 

import './css/styles.css';

function UserPage() {
  const [userData, setUserData] = useState(null);
  const [error, setError] = useState(null);
  const [books, setBooks] = useState([]);
  const [searchParams] = useSearchParams(); 

  useEffect(() => {
    const fetchUserData = async () => {
      const token = localStorage.getItem('accessToken');

      try {
        const response = await fetch('http://127.0.0.1:8000/users/me', {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`,  
          },
        });

        if (!response.ok) {
          throw new Error('Failed to fetch user data');
        }

        const data = await response.json();
        setUserData(data);

        // Fetch books after getting user data
        await fetchBooks(data.username);
      } catch (err) {
        setError(err.message);
      }
    };

    fetchUserData();
  }, []); // Only run on mount

  const fetchBooks = async (username) => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/users/books`, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('accessToken')}`,  
        },
      });

      if (!response.ok) {
        throw new Error('Failed to fetch books');
      }

      const booksData = await response.json();
      setBooks(booksData);
    } catch (error) {
      console.error("Error fetching books:", error);
    }
  };

  return (
    <>
      <Header />
      <main className="main">
        <div className="container">
          {error ? (
            <p className="loading-text" style={{ color: 'red' }}>{error}</p>
          ) : userData ? (
            <div className="user-info">
              <p>{userData.username}</p>
              <p><strong>Email:</strong> {userData.email}</p>
              <p><strong>Registration Date:</strong> {userData.registration_date || 'N/A'}</p>
            </div>
          ) : (
            <p className="loading-text">Loading user data...</p>
          )}
          <div className="books-grid">
            {books.length > 0 ? 
              books.map((book, index) => (
                <Link to={`/books/${book.book_name}`} key={index} className="book-container">
                  <BookPreview book={book} />
                </Link>
              )) 
              : <p className="loading-text">Loading books...</p>
            }
          </div>
        </div>
      </main>
      <Footer />
    </>
  );
}

export default UserPage;
