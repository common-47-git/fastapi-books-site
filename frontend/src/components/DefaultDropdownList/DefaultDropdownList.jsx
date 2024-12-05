import './styles.css';

function DefaultDropdownList({ listOfOptions, shelf, handleShelfChange }) {
  return (
    <select
      className="default-dropdown-list"
      value={shelf}
      onChange={handleShelfChange}
    >
      {/* Dynamically list the options, excluding "Put on the shelf" if it's selected */} 
      {listOfOptions
        .filter(option => option !== "put on the shelf" || shelf === "put on the shelf") // Exclude if not selected
        .map((option, index) => (
          <option
            className="default-dropdown-list__option"
            key={index}
            value={option.toLowerCase()} // Ensure value matches option's format
          >
            {option.toUpperCase()}
          </option>
      ))}
    </select>
  );
}

export default DefaultDropdownList;
