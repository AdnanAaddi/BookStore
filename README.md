# BookStore App

This Flask-based BookStore app allows users to sign up, log in. It also provides an admin panel for managing users and fetching book data from an external API.

## Features

- User Signup/Login:
  - Users can sign up with a username, email, and password.
  - Users can log in with their username and password.
  - Flask-Login is used for user session management.

- Admin Signup/Login:
  - Admins can sign up with a username, email, and password.
  - Admins can log in with their username and password.
  - Flask-Login is used for admin session management.

- Book Catalog:
  - Fetches book data from the provided external API.
  - Displays a list of books with all their information.

- Admin Panel:
  - Accessible only by admins.
  - Allows admins to view and manage user accounts.

## Project Structure

The project structure is organized as follows:

- `app.py`: Main Flask application file containing routes and configurations for Authentication system
- `books.py`: Contains functionality related to fetching book data from the external API.
- `templates/`: Directory containing HTML templates.

## Installation

1. Clone the repository and read the requirements.txt file for dependencies

