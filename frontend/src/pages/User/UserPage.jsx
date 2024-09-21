import { useEffect, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import Footer from '../../components/Footer/Footer';
import Header from '../../components/Header/Header';

function UserPage() {
  const [userData, setUserData] = useState(null);
  const [error, setError] = useState(null);
  const [searchParams] = useSearchParams(); 

  useEffect(() => {
    const fetchUserData = async () => {
      const username = searchParams.get('username'); 
      try {
        const token = localStorage.getItem('accessToken');

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
      } catch (err) {
        setError(err.message);
      }
    };

    fetchUserData();
  }, [searchParams]);

  return (
    <>
      <Header />
      <main className="main">
        {error ? (
          <p style={{ color: 'red' }}>{error}</p>
        ) : userData ? (
          <div>
            <h2>User Info</h2>
            <p><strong>Username:</strong> {userData.username}</p>
            <p><strong>Email:</strong> {userData.email}</p>
            <p><strong>Registration Date:</strong> {userData.registration_date || 'N/A'}</p>
            <p><strong>Disabled:</strong> {userData.disabled ? 'Yes' : 'No'}</p>
          </div>
        ) : (
          <p>Loading user data...</p>
        )}
      </main>
      <Footer />
    </>
  );
}

export default UserPage;
