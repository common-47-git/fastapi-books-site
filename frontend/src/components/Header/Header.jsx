import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import DefaultButton from '../DefaultButton/DefaultButton';
import './styles.css';

function HeaderComponent() {
  const [username, setUsername] = useState(null);
  const [loading, setLoading] = useState(true); // Add a loading state

  useEffect(() => {
    const fetchUsername = async () => {
      const token = localStorage.getItem("accessToken");
      if (token) {
        try {
          const response = await fetch("http://127.0.0.1:8000/users/me", {
            method: "GET",
            headers: {
              "Authorization": `Bearer ${token}`,
            },
          });

          if (response.ok) {
            const data = await response.json();
            setUsername(data.username);
          } else {
            console.error("Failed to fetch user data");
            setUsername(null);
          }
        } catch (error) {
          console.error("Error fetching user data:", error);
          setUsername(null);
        }
      }
      setLoading(false); // Set loading to false after fetch
    };

    fetchUsername();
  }, []);

  return (
    <header className="header">
      <div className="header-container">
        <div className="header-nav-left">
          <Link to={`/`} className="header-nav-el">
            <img src="../../public/main-icon.png" alt="icon" className="header-nav-icon" />
            Main
          </Link>
          <Link to={`/books`} className="header-nav-el">
            <img src="../../public/book-open-cover.png" alt="icon" className="header-nav-icon" />
            Books
          </Link>
        </div>
        <div className="header-nav-right">
          {loading ? (
              <div className="spinner"></div> // Placeholder loader
            ) : username ? (
              <Link to={`/users?username=${username}`} className="header-nav-el--user">
                <img src="../../public/profile-user.png" alt="icon" className="header-nav-icon" />
              </Link>
            ) : (
              <Link to={`/users/login`} className="header-nav-el">
                <DefaultButton content={"Login"} />
              </Link>
          )}
        </div>
      </div>
    </header>
  );
}

export default HeaderComponent;
