# Library Management System

A comprehensive desktop application for managing a library's book inventory and author information. Built with Python, Tkinter, and SQLite.

## Overview

The Library Management System is a user-friendly desktop application that allows librarians and bookstore owners to efficiently manage their inventory. It provides a complete CRUD (Create, Read, Update, Delete) interface for books and authors with a clean graphical user interface.

## Features

### 📚 Book Management
- **Add Books**: Register new books with title, quantity, author, and pricing
- **Update Books**: Modify book titles, quantities, prices, and author assignments
- **Delete Books**: Remove books from inventory with ID-based lookup
- **View All Books**: Display complete book catalog with author information
- **Search Books**: Find books by ID or partial title matching
- **Duplicate Prevention**: Automatic validation to prevent duplicate book IDs

### 👥 Author Management
- **Add Authors**: Register new authors with unique 4-digit IDs (1000-9999 range)
- **Update Authors**: Edit author details and information
- **View Authors**: See all registered authors in the system
- **Foreign Key Relationships**: Maintain data integrity between books and authors

### 🔍 Database Features
- **SQLite Backend**: Lightweight, file-based database storage
- **Data Validation**: Input validation for all entries
- **Query Optimization**: JOIN queries for efficient data retrieval
- **Automatic Schema**: Database and tables created automatically on startup
- **Referential Integrity**: Foreign key constraints between books and authors

## Technical Stack

- **Language**: Python 3.6+
- **GUI Framework**: Tkinter (built-in with Python)
- **Database**: SQLite 3
- **Architecture**: MVC-inspired with frame-based navigation

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Luvhani33f/Libary.git
   cd Libary
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Or manually install Tkinter (usually included with Python):
   ```bash
   # Windows
   python -m pip install tk
   
   # macOS
   brew install python-tk
   
   # Linux (Ubuntu/Debian)
   sudo apt-get install python3-tk
   ```

3. **Run the application**:
   ```bash
   python libay.py
   ```

## Usage

### Main Menu
On startup, the application displays the main menu with these options:

#### 1. **Add New Author**
   - Enter author ID (4 digits, 1000-9999)
   - Enter author name and details
   - Click "Add Author" to save

#### 2. **Add New Book**
   - Enter book ID (unique identifier)
   - Enter book title
   - Enter quantity available
   - Enter price
   - Select or enter author ID
   - Click "Add Book" to save

#### 3. **Update Book**
   - Enter book ID to search
   - Select field to update (title, quantity, price, or author)
   - Enter new value
   - Click "Update" to save changes

#### 4. **Delete Book**
   - Enter book ID to delete
   - Confirm deletion
   - Book removed from inventory

#### 5. **Search Books**
   - **By ID**: Enter exact book ID
   - **By Title**: Enter partial or full title for matching search
   - View search results with author information

#### 6. **View All Books**
   - Display complete catalog
   - Shows book ID, title, quantity, price, and author details
   - Data sorted by book ID

#### 7. **View All Authors**
   - Display all registered authors
   - Shows author ID and name

## Database Schema

### Authors Table
```sql
CREATE TABLE author (
    author_id INTEGER PRIMARY KEY,
    author_name TEXT NOT NULL
)
```

### Books Table
```sql
CREATE TABLE ebookstore (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    quantity INTEGER,
    price REAL,
    author_id INTEGER,
    FOREIGN KEY(author_id) REFERENCES author(author_id)
)
```

## Project Structure

```
Libary/
├── libay.py           # Main application file with GUI and database logic
├── requirements.txt   # Python dependencies
├── .gitignore         # Git ignore file
├── README.md          # Project documentation
└── library.db         # SQLite database (auto-created)
```

## Code Organization

The application is organized into logical sections:

- **Database Connection**: SQLite connection management with WAL mode
- **Frame Classes**: Tkinter frame subclasses for different screens
- **Menu Navigation**: Main menu with button-based navigation
- **CRUD Operations**: Separate methods for Create, Read, Update, Delete
- **Validation**: Input validation and error handling

## Key Functions

### Database Operations
- `connect_database()`: Establish SQLite connection
- `add_author()`: Insert new author record
- `add_book()`: Insert new book with validation
- `update_book()`: Modify existing book details
- `delete_book()`: Remove book by ID
- `search_by_id()`: Find book by ID
- `search_by_title()`: Find books by partial title match
- `view_all_books()`: Display complete catalog

### UI Management
- `FrameMain()`: Main menu screen
- `FrameAuthor()`: Author management screen
- `FrameBook()`: Book management screen
- `FrameUpdate()`: Book update screen
- `FrameDelete()`: Book deletion screen
- `FrameSearch()`: Book search screen

## Error Handling

The application includes comprehensive error handling:
- **Validation Errors**: Input format and range validation
- **Database Errors**: Connection and query error handling
- **Duplicate Prevention**: Checks for existing book IDs
- **User Feedback**: Error message dialogs with clear messages

## Future Enhancements

- [ ] Export to CSV/PDF reports
- [ ] Advanced search filters (by author, price range, quantity)
- [ ] Inventory alerts (low stock warnings)
- [ ] Book categories and genres
- [ ] User authentication and roles
- [ ] Multi-user database support
- [ ] API for external integrations
- [ ] Mobile app companion
- [ ] Automated backups
- [ ] Statistical analytics and reports

## Performance Considerations

- **Database Indexing**: Book ID and author ID indexed for faster queries
- **Query Optimization**: Uses JOIN queries for efficient data retrieval
- **WAL Mode**: Enables concurrent read-write operations
- **Lazy Loading**: Data loaded on demand from GUI screens

## Known Limitations

- Single-threaded GUI (can freeze during long operations)
- Limited to local database (no network support)
- No built-in user authentication
- No audit trail or change history
- Single-file application (could benefit from modularization)

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes with clear commit messages
4. Push to the branch (`git push origin feature/improvement`)
5. Submit a Pull Request

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support & Issues

Found a bug or have a feature request? Please open an issue on the GitHub repository:
- Bug Reports: https://github.com/Luvhani33f/Libary/issues
- Feature Requests: https://github.com/Luvhani33f/Libary/issues

## Author

**Luvhani33f** - Initial development and maintenance

## Acknowledgments

- Built with Python and Tkinter
- SQLite for reliable data storage
- Community feedback and contributions

---

**Version**: 1.0.0  
**Last Updated**: 2026-07-15  
**Status**: Active Development
