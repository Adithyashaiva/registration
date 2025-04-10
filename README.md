# Registration Table and CRUD Operations.

A Django-based web application to manage registrations with Create, Read, Update, and Delete (CRUD) functionality. The project uses a MySQL database and includes an interactive user interface built with HTML, CSS, and JavaScript.

## Features

- User-friendly interface for managing registrations.
- CRUD operations:
  - **Create**: Add new registration records.
  - **Read**: View all registration records in a table format.
  - **Update**: Edit existing registration records.
  - **Delete**: Remove registration records.
- Form validation on both frontend and backend.
- MySQL database integration for reliable data storage.
- Responsive design for cross-device compatibility.


## Technologies Used

- **Backend**: Django Framework
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL
- **Styling**: Unique CSS files for each page
- **Version Control**: Git and GitHub


## Project Structure

registration-management-system/
├── registration/                  # Django project directory
│   ├── settings.py                # Project settings
│   ├── urls.py                    # Project URL configurations
│   ├── wsgi.py                    # WSGI application
├── project/                       # Django app directory
│   ├── models.py                  # Database models
│   ├── views.py                   # Application views
│   ├── forms.py                   # Form validation
│   ├── urls.py                    # App URL configurations
│   ├── templates/                 # HTML templates
│   │   ├── create_registration.html
│   │   ├── view_registrations.html
│   │   ├── update_registration.html
│   │   ├── delete_registration.html
│   ├── static/                    # Static files (CSS, JS)
│       ├── css/
│           ├── create_registration.css
│           ├── view_registrations.css
│           ├── update_registration.css
│           ├── delete_registration.css
├── db.sqlite3                     # SQLite database (if used for development)
├── manage.py                      # Django management script
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation


Make any changes in database:
   python manage.py makemigrations
   python manage.py migrate


To runserver:

---> cd registration
---> py manage.py runserver  / python manage.py runserver



