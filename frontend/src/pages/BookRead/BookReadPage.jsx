import { useEffect, useState } from "react";
import { useLocation, useParams, Link } from "react-router-dom";
import axios from "axios";

import Header from '../../components/Header/Header';

function ChapterDetail() {
  const { bookName } = useParams();
  const location = useLocation();
  const query = new URLSearchParams(location.search);
  const [chapterContent, setChapterContent] = useState(null);
  const [error, setError] = useState(null);
  const volume = query.get('volume') || 1;
  const chapter = query.get('chapter') || 1;

  useEffect(() => {
    axios.get(`http://127.0.0.1:8000/books/${bookName}/read`, {
      params: { volume: volume, chapter: chapter }
    })
    .then(response => {
      if (response.data) {
        setChapterContent(response.data);
        setError(null); // Clear any previous errors
      } else {
        // Handle case where chapter data is empty or not found
        setChapterContent(null);
        setError("Chapter not found.");
      }
    })
    .catch(error => {
      console.error("There is no such chapter:", error);
      setChapterContent(null);
      setError("Error fetching chapter.");
    });
  }, [bookName, volume, chapter]);

  const chapterNumber = parseInt(chapter, 10);

  // Calculate chapter for the Previous link
  const previousChapter = chapterNumber > 1 ? chapterNumber - 1 : null;

  // Calculate chapter for the Next link
  const nextChapter = chapterNumber + 1;

  return (
    <>  
      <Header />
      <main className="main">
        <div className="chapter-detail-container">
          {error ? (
            <p>{error}</p> // Display error message if there is one
          ) : (
            <>
              <h1>Chapter {chapter}</h1>
              <div>{chapterContent}</div>
            </>
          )}
        </div>
      </main>
      {previousChapter !== null && (
        <Link to={{
          pathname: `/books/${bookName}/read`,
          search: `?volume=${volume}&chapter=${previousChapter}`,
        }}>
          Previous
        </Link>
      )}
      <Link to={{
        pathname: `/books/${bookName}/read`,
        search: `?volume=${volume}&chapter=${nextChapter}`,
      }}>
        Next
      </Link>
    </>
  );
}

export default ChapterDetail;
