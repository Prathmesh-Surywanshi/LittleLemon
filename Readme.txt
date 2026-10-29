Little Lemon Restaurant - Django REST API

SETUP
1. python -m venv venv  &&  venv\Scripts\activate
2. pip install -r requirements.txt
3. Create MySQL database: CREATE DATABASE littlelemon;
4. Update DB user/password in littlelemon/settings.py
5. python manage.py migrate
6. python manage.py runserver

API PATHS TO TEST
/
/admin/
/auth/users/
/auth/users/me/
/auth/token/login/
/api/menu/
/api/menu/1/
/api/bookings/

NOTES
- Menu: GET is public; POST/PUT/DELETE need token.
- Bookings: all methods need header  Authorization: Token <token>
- Run unit tests: python manage.py test
