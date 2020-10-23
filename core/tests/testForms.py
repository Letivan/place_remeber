from django.contrib.auth.models import User
from django.test import TestCase

from core.forms import RememberForm


class AddRememberFormTest(TestCase):
    """Testing form add user remember"""
    def test_AddRemember_valid(self):
        user = User.objects.create_user(username='TestUser', email='1407navi@gmail.com', password='F123456*')
        form = RememberForm(data={'user': user, 'remember': "Test remember", 'coordinate_0': "56.83251718208333",
                                  'coordinate_1': "60.57350635528565"})
        self.assertTrue(form.is_valid())
