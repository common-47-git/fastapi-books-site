import '../App.css';
import { useEffect, useState } from "react";
import axios from "axios";
import { useLocation, useParams } from "react-router-dom";

import Header from '../components/Header';

function ChapterDetail() {
  const { bookName } = useParams();
  const location = useLocation();
  const query = new URLSearchParams(location.search);
  const [chapterContent, setChapterContent] = useState(null);
  const volume = query.get('volume') || 1;
  const chapter = query.get('chapter') || 1;

  useEffect(() => {
    axios.get(`http://127.0.0.1:8000/books/${bookName}/read`, {
      params: { volume: volume, chapter: chapter }
    })
    .then(response => {
      setChapterContent(response.data);
    })
    .catch(error => {
      console.error("Error fetching chapter:", error);
    });
  }, [bookName, volume, chapter]);

  return (
    <>  
      <Header></Header>
      <main className="main">
        <div className="chapter-detail-container">
          <h1>Chapter {chapter}</h1>
          <div>{chapterContent}</div>
        </div>
      </main>
    </>
  );
}

export default ChapterDetail;
