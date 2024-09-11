import { useState } from "react";

import Header from '../../components/Header/Header';
import Footer from '../../components/Footer/Footer';
import './css/styles.css';

function UserLogin() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch("/users/login", {
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
      // Handle the token (e.g., save it to localStorage)
      console.log("Access token:", data.access_token);
    } else {
      // Handle errors (e.g., show error message)
      console.error("Login failed");
    }
  };

  return (
    <>
        <Header></Header>
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
        <Footer></Footer>
    </>
  );
}

export default UserLogin;
