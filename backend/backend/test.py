from django.test import TestCase, Client
from django.urls import reverse

from .views import main


class ViewsTest(TestCase):

    def setUp(self) -> None:
        self.guest_client = Client()

    def post_request(self, date):
        response = self.guest_client.post(
            reverse('main'), {'date': date}
        ).context['weeks']
        return response

    def test_start_week(self):
        self.assertEqual(self.post_request('2019-01-05'), 1)

    def test_next_week(self):
        self.assertEqual(self.post_request('2019-01-07'), 2)

    def test_last_week_of_year(self):
        self.assertEqual(self.post_request('2019-12-30'), 53)

    def test_week_with_next_year(self):
        self.assertEqual(self.post_request('2020-12-30'), 105)
