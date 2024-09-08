import { Link } from "react-router-dom";
import './styles.css';

function HeaderComponent() {
  return (
      <header className="header">
        <nav className="header-nav">
          <Link to={`/`} className="header-nav-el"> Main </Link>
          <Link to={`/books`} className="header-nav-el"> Books </Link>
        </nav>
      </header>
  );
}

export default HeaderComponent;

