import './styles.css';

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-content">
        <p>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Dicta deleniti incidunt, 
          fugit velit enim tenetur voluptatem sint eveniet eligendi suscipit saepe culpa, 
          id impedit nulla a quas fuga molestiae ipsa.
        </p>
        <div className="footer-links">
          <a href="/privacy-policy" className="footer-link">Privacy Policy</a>
          <a href="/terms-of-service" className="footer-link">Terms of Service</a>
          <a href="/contact" className="footer-link">Contact Us</a>
        </div>
      </div>
      <div className="footer-bottom">
        <p>&copy; {new Date().getFullYear()} Your Company Name. All rights reserved.</p>
      </div>
    </footer>
  );
}

export default Footer;
