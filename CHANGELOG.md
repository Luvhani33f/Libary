# Changelog

All notable changes to the Library Management System will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-07-15

### Added
- **Core Features**
  - Book management (add, update, delete, view all)
  - Author management (add, update, view all)
  - Search functionality (by ID and title)
  - SQLite database with proper schema
  - Tkinter-based GUI interface

- **Database Features**
  - Foreign key relationships between books and authors
  - Input validation for all entries
  - Automatic database initialization
  - Author ID validation (4-digit format: 1000-9999)
  - Duplicate prevention for book IDs

- **Documentation**
  - Comprehensive README with features and usage
  - Installation and setup guide
  - Database schema documentation
  - Contributing guidelines
  - MIT License

- **Project Files**
  - requirements.txt with dependencies
  - .gitignore for version control
  - CHANGELOG tracking

### Features
- [x] Add new authors
- [x] Add new books with author assignment
- [x] Update book information (title, quantity, price, author)
- [x] Delete books from inventory
- [x] Search books by ID
- [x] Search books by title
- [x] View all books with author details
- [x] View all authors
- [x] Input validation and error handling
- [x] GUI-based interface with frame navigation

## Planned Features (Future Releases)

### v1.1.0 - Planned
- [ ] Export to CSV
- [ ] Book categories and genres
- [ ] Inventory alerts (low stock warnings)
- [ ] Advanced filtering and sorting
- [ ] Book cover images

### v1.2.0 - Planned
- [ ] User authentication and roles
- [ ] Audit trail and change history
- [ ] Statistical reports and analytics
- [ ] Data import/export functionality
- [ ] Multi-database support

### v2.0.0 - Long-term
- [ ] Web interface
- [ ] Mobile app
- [ ] REST API
- [ ] Real-time synchronization
- [ ] Cloud backup and restore

## Known Issues

### Current Version
- GUI can freeze on long operations (single-threaded)
- Limited to local database access
- No built-in user authentication
- Single-file application

### Workarounds
- Keep operations simple to avoid freezing
- Run on local machine only
- Implement external authentication if needed
- Consider refactoring to modules for large-scale extension

## Version History

### [0.1.0] - Initial Development
- Basic CRUD operations
- Simple Tkinter interface
- SQLite database backend
- Author and book management

---

## How to View Changes

### Between Versions
```bash
git log --oneline v1.0.0..HEAD
git diff v1.0.0 HEAD
```

### For Specific Commits
```bash
git show COMMIT_HASH
git log --name-status -1 COMMIT_HASH
```

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Feedback

Have suggestions for improvements? Open an issue on GitHub:
- Bug reports: https://github.com/Luvhani33f/Libary/issues
- Feature requests: https://github.com/Luvhani33f/Libary/issues

---

**Latest Version**: 1.0.0  
**Last Updated**: 2026-07-15  
**Maintained By**: Luvhani33f
