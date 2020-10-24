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
        """If user is not autheticated - get page login return code 200, not 301"""
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_page_authenticated(self):
        """If user is autheticated - get page login return redirect on home page"""
        c = Client()
        c.login(username='test', password='password123*')
        response = c.get('/login/')
        self.assertRedirects(response, '/')

    def test_home_page_authenticated(self):
        """If user is autheticated - get page home return code 200, not 301"""
        c = Client()
        c.login(username='test', password='password123*')
        response = c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_anonymous(self):
        """If user is not autheticated - get page home return redirect on login page"""
        response = self.client.get('/', follow=True)
        self.assertRedirects(response, '/login/')

    def test_context_home_page(self):
        """If user is autheticated context return remembers in context on home page"""
        c = Client()
        c.login(username='test', password='password123*')
        response = c.get('/')
        self.assertIsNotNone(response.context['remembers'])

    def test_addremember_page_anonymous(self):
        """If user is not autheticated - get page addremember return redirect on login page"""
        response = self.client.get('/addremember/')
        self.assertRedirects(response, '/login/')

    def test_addremember_page_authenticated(self):
        """If user is autheticated - get page addremember return code 200, not 301"""
        c = Client()
        c.login(username='test', password='password123*')
        response = c.get('/addremember/')
        self.assertEqual(response.status_code, 200)

    def test_addremember_form_is_valid(self):
        c = Client()
        c.login(username='test', password='password123*')
        response = c.post('/addremember/', {'remember': "Test remember", 'coordinate': "56.83251718208333"})
        self.assertEqual(response.status_code, 200)


# class NewPatientFormTest(TestCase):
#
#     def setUp(self):
#         self.form_data = {
#             'name': 'Billy',
#             'surname': 'Masters',
#             'phone': '123-358-2382',
#         }
