# Library Management System using Django

This is a Library Management System developed using Django, a Python web framework. The system allows users to view a collection of books, add new books, and view detailed information about a particular book.

## Features

- User Authentication: Users need to log in to access certain functionalities.
- Dashboard: Displays a list of available books.
- Book Detail Page: Provides detailed information about a selected book.
- Add New Book: Allows users to add new books to the library.
- Book Information: Each book includes details such as name, author, description, rating, release date, cover photo, and book file.

## Getting Started

1. Clone this repository to your local machine.
2. Create a virtual environment and activate it.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the development server using `python manage.py runserver`.
5. Access the application through your web browser at `http://localhost:8000/`.

## Code Explanation

The project is organized into the following components:

- `books` App: This app manages the core functionalities of the library system.

  - `models.py`: Defines the `Books` model with fields such as name, author, description, rating, release date, cover photo, and book file.

  - `views.py`: Contains view functions for rendering the dashboard, book detail page, and adding new books.

  - `urls.py`: Defines URL patterns for different views.

- `templates` Directory: Contains HTML templates for rendering the web pages.

- `media` Directory: Stores uploaded cover photos and book files.

- `settings.py`: Includes project settings, such as installed apps, database configurations, authentication settings, and media file settings.

## Usage

1. Run the development server.
2. Visit the dashboard at `/`.
3. Log in with your credentials.
4. Browse through the list of available books on the dashboard.
5. Click on a book to view its detailed information.
6. To add a new book, visit `/addbook/` and fill in the required information.

## Requirements

- Python 3.x
- Django 3.x
- Other dependencies listed in `requirements.txt`

## Contributing

Contributions are welcome! If you find any issues or want to enhance the system, feel free to open a pull request or issue on the repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy reading and managing your library with Django!
