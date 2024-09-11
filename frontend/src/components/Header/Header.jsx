import { Link } from "react-router-dom";
import DefaultButton from '../DefaultButton/DefaultButton';
import './styles.css';

function HeaderComponent() {
  return (
      <header className="header">
        <nav className="header-nav">
          <Link to={`/`} className="header-nav-el">  Main </Link>
          <Link to={`/books`} className="header-nav-el"> <img src="../../public/book-open-cover.png" alt="icon" className="header-nav-icon" content="Books"/> Books </Link>
          <Link to={`/users/login`} className="header-nav-el"> <DefaultButton content={"Login"} ></DefaultButton> </Link> 
        </nav>
      </header>
  );
}

export default HeaderComponent;

