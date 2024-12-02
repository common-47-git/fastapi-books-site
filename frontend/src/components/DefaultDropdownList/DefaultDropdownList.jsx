import './styles.css';

function DefaultDropdownList({ listOfOptions, shelf, handleShelfChange }) {
  return (
      <select className="default-dropdown-list" value={shelf} onChange={handleShelfChange}>
        {/* Dynamically list the options */}
        {listOfOptions.map((option, index) => (
          <option key={index} value={option.toLowerCase()}>
            {option.toUpperCase()}
          </option>
        ))}
      </select>
  );
}

export default DefaultDropdownList;
