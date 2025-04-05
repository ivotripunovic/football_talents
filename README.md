# Football Manager Application

A Django-based web application for managing football players' profiles and information. This application allows users to register, create player profiles, and manage their football-related information.

## Features

- User Authentication
  - Registration with email verification
  - Login/Logout functionality
  - Password reset capability

- Player Profile Management
  - Personal Information
    - Name
    - Date of Birth
    - Nationality
  - Physical Attributes
    - Height (in centimeters)
    - Weight (in kilograms)
  - Football-specific Information
    - Position (Goalkeeper, Defender, Midfielder, Forward)
    - Preferred Foot (Left, Right, Both)
    - Jersey Number
  - Performance Ratings
    - Speed (1-100)
    - Strength (1-100)
    - Stamina (1-100)

- Admin Interface
  - Custom admin view for Player model
  - Advanced filtering and search capabilities
  - Organized display of player information

## Technical Specifications

- Python 3.x
- Django 5.1.7
- Bootstrap 5.3.0
- django-crispy-forms
- SQLite Database

## Setup Instructions

1. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/Mac
# or
.\venv\Scripts\activate  # On Windows
```

2. Install required packages:
```bash
pip install django django-crispy-forms crispy-bootstrap5
```

3. Apply database migrations:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

4. Create superuser (admin):
```bash
python3 manage.py createsuperuser
```

5. Run the development server:
```bash
python3 manage.py runserver
```

## Application URLs

- Home: http://127.0.0.1:8000/
- Registration: http://127.0.0.1:8000/players/register/
- Login: http://127.0.0.1:8000/accounts/login/
- Profile: http://127.0.0.1:8000/players/profile/
- Edit Profile: http://127.0.0.1:8000/players/profile/edit/
- Admin Interface: http://127.0.0.1:8000/admin/

## Project Structure

```
football_manager/
├── football_manager/     # Project settings
├── players/             # Main application
│   ├── templates/      # HTML templates
│   ├── models.py       # Database models
│   ├── views.py        # View logic
│   ├── forms.py        # Form definitions
│   ├── urls.py         # URL routing
│   └── admin.py        # Admin interface configuration
└── manage.py           # Django management script
```

## Security Considerations

- Password validation enabled
- CSRF protection
- Login required for profile access
- Secure password handling

## Development

The application uses:
- Bootstrap for responsive design
- Crispy Forms for form styling
- Django's built-in authentication system
- SQLite as the default database

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 