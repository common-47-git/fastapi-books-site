import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import Header from '../../components/Header/Header';
import Footer from '../../components/Footer/Footer';
import './css/styles.css';

function UserLogin() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate(); // Hook to programmatically navigate

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch("http://127.0.0.1:8000/users/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: new URLSearchParams({
        username: username,
        password: password,
      }),
    });
  
    if (response.ok) {
      const data = await response.json();
      localStorage.setItem("accessToken", data.access_token);
      console.log("Access token:", data.access_token);
      navigate('/');
    } else {
      console.error("Login failed");
    }
  };  

  return (
    <>
      <Header />
      <main className="main">
        <form onSubmit={handleSubmit}>
          <label>
            Username:
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </label>
          <br />
          <label>
            Password:
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </label>
          <br />
          <button type="submit">Login</button>
        </form>
      </main>
      <Footer />
    </>
  );
}

export default UserLogin;
