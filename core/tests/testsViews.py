from django.test import TestCase


class TestView(TestCase):
    def test_login(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_home_deny_anonymous(self):
        response = self.client.get('/', follow=True)
        self.assertRedirects(response, '/login/')

    def test_home_add_remember_deny_anonymous(self):
        response = self.client.get('/addremember/', follow=True)
        self.assertRedirects(response, '/login/')
