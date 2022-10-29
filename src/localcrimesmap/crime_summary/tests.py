from django.test import TestCase

class CallsTest(TestCase):
    def test_summary_call(self):
        response = self.client.get('/summary', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'crime_summary/summary.html')
