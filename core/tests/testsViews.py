import base64

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.test import TestCase, Client


class TestView(TestCase):
    def setUp(self):
        self.username = 'test'
        self.email = 'test@client.client'
        self.password = 'password123*'
        self.user = User.objects.create_user(
            self.username, self.email, self.password
        )

    def test_login_page_anonimous(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_page_authenticated(self):
        c = Client()
        c.login(username='test', password='password123*')
        response = c.get('/login/')
        self.assertRedirects(response, '/')

    def test_home_allow_authenticated(self):
        c = Client()
        c.login(username='test', password='password123*')
        response = c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_deny_anonymous(self):
        response = self.client.get('/', follow=True)
        self.assertRedirects(response, '/login/')

    def test_home_add_remember_anonymous(self):
        response = self.client.get('/addremember/')
        self.assertRedirects(response, '/login/')

    def test_home_add_remember_authenticated(self):
        c = Client()
        c.login(username='test', password='password123*')
        response = c.get('/addremember/')
        self.assertEqual(response.status_code, 200)
    #
    # def test_context(self):
    #     # GET response using the test client.
    #     response = self.client.get('/list/ofitems/')
    #     # response.context['your_context']
    #     self.assertIsNone(response.context['page_obj'])
    #     self.assertIsNone(response.context['customer'])
