# Contributing to Library Management System

Thank you for your interest in contributing to the Library Management System! This document provides guidelines and instructions for contributing.

## Code of Conduct

Be respectful, inclusive, and professional in all interactions.

## Getting Started

### 1. Fork and Clone
```bash
git clone https://github.com/YOUR_USERNAME/Libary.git
cd Libary
```

### 2. Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
# or for bug fixes:
git checkout -b fix/bug-description
```

### 3. Set Up Development Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Development Standards

### Code Style
- Follow PEP 8 Python style guidelines
- Use 4 spaces for indentation
- Keep lines under 100 characters where possible
- Use descriptive variable and function names

### Format Code
```bash
black libay.py
```

### Lint Code
```bash
pylint libay.py
```

## Types of Contributions

### Bug Reports
- **Title**: Clearly describe the bug
- **Steps to Reproduce**: Step-by-step instructions
- **Expected vs Actual**: What should happen vs what does happen
- **Screenshots**: Include if GUI-related
- **System Info**: Python version, OS, database state if relevant

### Feature Requests
- **Title**: Brief description of feature
- **Use Case**: Why is this feature needed?
- **Proposed Solution**: How should it work?
- **Alternatives**: Any alternative approaches?

### Code Improvements
- Performance optimizations
- Code refactoring for clarity
- Additional error handling
- Test coverage improvements

### Documentation
- Typo fixes in README
- Clearer explanations
- Additional examples
- Better API documentation

## Commit Guidelines

- **Clear Messages**: Write descriptive commit messages
- **One Feature**: Keep commits focused on one change
- **Prefix**: Use prefixes for clarity:
  - `feat:` New feature
  - `fix:` Bug fix
  - `docs:` Documentation
  - `refactor:` Code restructuring
  - `test:` Test additions
  - `perf:` Performance improvements

### Example Commits
```bash
git commit -m "feat: Add book category filtering"
git commit -m "fix: Prevent duplicate author IDs in update"
git commit -m "docs: Add database schema documentation"
```

## Pull Request Process

### Before Submitting
- [ ] Code follows project style guidelines
- [ ] Code formatted with `black`
- [ ] Code passes `pylint` checks
- [ ] Tests pass (if applicable)
- [ ] Changes are well-documented
- [ ] README updated if needed
- [ ] No breaking changes to existing functionality

### PR Description Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Related Issues
Fixes #(issue number)

## Testing
How to test these changes:
1. Step 1
2. Step 2

## Screenshots (if applicable)
Include before/after screenshots

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have performed a self-review
- [ ] I have commented complex areas
- [ ] I have updated the README
```

## Review Process

1. **Automated Checks**: Code style and lint checks run automatically
2. **Code Review**: Maintainers review for quality, security, and compatibility
3. **Testing**: Changes tested for functionality and edge cases
4. **Feedback**: Any requested changes are addressed
5. **Merge**: Once approved, your PR is merged

## Areas for Contribution

### High Priority
- [ ] User authentication system
- [ ] Database backup and recovery
- [ ] Advanced search and filtering
- [ ] Bulk import/export functionality
- [ ] Unit test suite

### Medium Priority
- [ ] UI/UX improvements
- [ ] Performance optimizations
- [ ] Code documentation enhancement
- [ ] Example data scripts
- [ ] API documentation

### Welcome Contributions
- Bug reports and fixes
- Documentation improvements
- Code cleanup
- Test additions
- Feature ideas and discussions

## Development Workflow

### For Bug Fixes
```bash
git checkout main
git pull origin main
git checkout -b fix/bug-name
# ... make changes ...
git add .
git commit -m "fix: Brief description"
git push origin fix/bug-name
# Create PR on GitHub
```

### For Features
```bash
git checkout main
git pull origin main
git checkout -b feature/feature-name
# ... make changes ...
git add .
git commit -m "feat: Brief description"
git push origin feature/feature-name
# Create PR on GitHub
```

## Questions or Need Help?

- **Issues**: Use GitHub Issues for questions, suggestions, or problems
- **Discussions**: Start a discussion for ideas and design decisions
- **Email**: Reach out to the maintainer if needed

## Recognition

Contributors are recognized in:
- README contributors section
- Release notes
- GitHub contributors page

---

**Thank you for contributing to make this project better!**
