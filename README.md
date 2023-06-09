# Flask Python Web Application

This repository contains a Flask web application built using Python. The application is designed to showcase the basic features and functionality of Flask, a lightweight web framework. It serves as a starting point for building your own Flask-based projects.

## Features

- Simple and intuitive Flask application structure
- Basic CRUD operations (Create, Read, Update, Delete)
- Routing and URL handling using Flask routes
- Rendering HTML templates with Jinja2 templating engine
- Form handling and validation with Flask-WTF
- Database integration with Flask-SQLAlchemy
- User authentication and session management
- Bootstrap for responsive and modern UI design

## Requirements

- Python 3.x
- Flask
- Flask-WTF
- Flask-SQLAlchemy

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/Mgobeaalcoba/flask_python.git
```

2. Change into the project directory:

```bash
cd flask_python
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Set up the database:

```bash
python manage.py create_db
```

5. Run the application:

```bash
flask run
```

6. Open your web browser and visit `http://localhost:5000` to see the application in action.

## Project Structure

The project structure follows the recommended Flask application structure:

- `app`: This directory contains the main Flask application code.
  - `static`: Static assets such as CSS, JavaScript, and images.
  - `templates`: HTML templates for rendering the views.
  - `forms.py`: Flask-WTF forms for handling user input and validation.
  - `models.py`: Database models using Flask-SQLAlchemy.
  - `routes.py`: Flask routes for handling different URL endpoints.
- `migrations`: Database migration scripts generated by Flask-Migrate.

## Contributing

Contributions to this Flask Python web application are always welcome. Here are a few ways you can help:

- Report bugs and issues
- Suggest new features and enhancements
- Fix bugs and submit pull requests

Please make sure to follow the existing code style and conventions when making contributions.

## License

This project is licensed under the [MIT License](LICENSE).
