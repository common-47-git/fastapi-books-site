import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import DefaultButton from '../DefaultButton/DefaultButton';
import './styles.css';

function HeaderComponent() {
  const [username, setUsername] = useState(null);

  useEffect(() => {
    const fetchUsername = async () => {
      const token = localStorage.getItem("accessToken"); // Get the access token
      if (token) {
        try {
          const response = await fetch("http://127.0.0.1:8000/users/me", {
            method: "GET",
            headers: {
              "Authorization": `Bearer ${token}`, // Include the token in the header
            },
          });

          if (response.ok) {
            const data = await response.json();
            setUsername(data.username); // Set the username from the response
          } else {
            console.error("Failed to fetch user data");
            setUsername(null); // Reset username on error
          }
        } catch (error) {
          console.error("Error fetching user data:", error);
          setUsername(null); // Reset username on error
        }
      }
    };

    fetchUsername();
  }, []); // Fetch username on component mount

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
          {username ? ( // Conditionally render based on username
            <Link to={`/users?username=${username}`} className="header-nav-el--user"> <img src="../../public/profile-user.png" alt="icon" className="header-nav-icon" /> </Link>
          ) : (
            <Link to={`/users/login`} className="header-nav-el"> <DefaultButton content={"Login"} /> </Link>
          )}
        </div>
      </div>
    </header>
  );
}

export default HeaderComponent;
