from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from .models import Menu, Booking

class MenuModelTest(TestCase):
    def test_menu_str(self):
        item = Menu.objects.create(title="Greek Salad", price=12.50, inventory=10)
        self.assertEqual(str(item), "Greek Salad")

class BookingModelTest(TestCase):
    def test_booking_str(self):
        b = Booking.objects.create(name="Anita", no_of_guests=4,
                                   booking_date="2026-11-10T19:30:00Z")
        self.assertEqual(str(b), "Anita")

class ApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="tester", password="Pass@12345")
        self.token = Token.objects.create(user=self.user)

    def test_menu_list_public(self):
        Menu.objects.create(title="Pasta", price=10, inventory=5)
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, 200)

    def test_bookings_requires_auth(self):
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, 401)

    def test_create_booking_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {"name": "Ravi", "no_of_guests": 2, "booking_date": "2026-11-12T20:00:00Z"}
        response = self.client.post('/api/bookings/', data, format='json')
        self.assertEqual(response.status_code, 201)
