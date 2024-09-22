import { useEffect, useState } from "react";
import { useLocation, useParams, Link, useNavigate } from "react-router-dom";
import axios from "axios";

import Header from '../../components/Header/Header';
import './css/styles.css'

function BookReadPage() {
  const { bookName } = useParams();
  const location = useLocation();
  const navigate = useNavigate(); // Use navigate for redirect
  const query = new URLSearchParams(location.search);
  const [chapterContent, setChapterContent] = useState(null);
  const volume = query.get('volume') || 1;
  const chapter = query.get('chapter') || 1;

  useEffect(() => {
    axios.get(`http://127.0.0.1:8000/books/${bookName}/read`, {
      params: { volume: volume, chapter: chapter }
    })
    .then(response => {
      if (response.data) {
        setChapterContent(response.data);
      } else {
        // Redirect to the 404 page if no data is found
        navigate('/404');
      }
    })
    .catch(error => {
      if (error.response && error.response.status === 404) {
        navigate('/404'); // Redirect to the 404 page on error
      }
    });
  }, [bookName, volume, chapter, navigate]);

  const chapterNumber = parseInt(chapter, 10);
  const previousChapter = chapterNumber > 1 ? chapterNumber - 1 : 1;
  const nextChapter = chapterNumber + 1;

  return (
    <>  
      <Header />
      <main className="main">
        <div className="container">
          <div className="chapter-container">
            <h1>Chapter {chapter}</h1>
            <div className="chapter-text">{chapterContent}</div>

            <div className="chapter-nav">
              {chapter > 1 && (
                <Link 
                  to={{
                    pathname: `/books/${bookName}/read`,
                    search: `?volume=${volume}&chapter=${previousChapter}`,
                  }} 
                  className="chapter-link"
                >
                  Previous
                </Link>
              )}
              <Link to={{
                pathname: `/books/${bookName}/read`,
                search: `?volume=${volume}&chapter=${nextChapter}`,
              }} className="chapter-link">
                Next
              </Link>
            </div>
          </div>
        </div>
      </main>
    </>
  );
}

export default BookReadPage;
