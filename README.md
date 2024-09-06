# Vinyl Store Django Project

## Overview
This project is a web application for a vinyl record store built using Django. It allows users to browse a collection of vinyl albums, view details, add items to a cart, and make purchases. The application also includes features for user registration, login, and a simple inventory management system.

## Features
- Browse album catalog with cover art display
- User registration and authentication
- Shopping cart functionality
- Search albums by title, artist, or keywords
- Admin interface for inventory management
- Responsive design for mobile and desktop viewing

## Technologies Used
- Django 3.x
- Python 3.x
- HTML5
- CSS3
- Bootstrap 5
- JavaScript (for cart interactions)
- SQLite (database)

## Setup and Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/vinyl-store-project.git
   ```
2. Navigate to the project directory:
   ```
   cd vinyl-store-project
   ```
3. Create a virtual environment:
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
6. Run migrations:
   ```
   python manage.py migrate
   ```
7. Load initial album data:
   ```
   python manage.py load_albums
   ```
8. Create a superuser:
   ```
   python manage.py createsuperuser
   ```
9. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage
- Visit `http://localhost:8000` to view the homepage
- Browse albums, add them to your cart, and proceed to checkout
- Use the admin interface at `http://localhost:8000/admin` to manage inventory

## Project Structure
- `shop/` - Main application directory
  - `models.py` - Database models
  - `views.py` - View functions
  - `urls.py` - URL configurations
  - `forms.py` - Form definitions
  - `admin.py` - Admin interface configurations
  - `templates/` - HTML templates
  - `static/` - Static files (CSS, JS, images)
- `vinyl_store/` - Project settings directory

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.
## Contact
For any queries regarding this project, please contact at leahsigana47@gmail.com
