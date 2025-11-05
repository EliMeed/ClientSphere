
"""
Basic smoke test to confirm the app loads.
"""

from django.test import TestCase

class BasicAppTest(TestCase):
    def test_home_page_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
