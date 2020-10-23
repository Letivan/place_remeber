from django.test import TestCase

from core.templatetags.tags import intdot


class TestFilters(TestCase):

    def test_filter_intdot(self):
        self.assertEqual(intdot('50,1'), '50.1')
