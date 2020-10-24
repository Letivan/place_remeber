from django.test import TestCase, Client

from core.models import Remember


class RememberModelTest(TestCase):

    def test_string_representation(self):
        remember = Remember(remember="My remembr body", coordinate='12345')
        self.assertEqual(str(remember), str(remember.id))

    def test_verbose_name_plural(self):
        self.assertEqual(str(Remember._meta.verbose_name_plural), "Воспоминания")

    def test_verbose_name(self):
        self.assertEqual(str(Remember._meta.verbose_name), "Воспоминание")
