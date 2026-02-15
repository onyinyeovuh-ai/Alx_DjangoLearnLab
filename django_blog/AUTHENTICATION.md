Authentication System Documentation

Features Implemented:
- User registration using extended UserCreationForm with email.
- Login using Django built-in LoginView.
- Logout functionality.
- Profile management allowing user to edit username and email.

How to Run:
1. python manage.py migrate
2. python manage.py runserver
3. Visit /register, /login, /profile

Security:
- CSRF tokens used in all forms.
- Passwords handled using Django hashing.
- Login required for profile page.