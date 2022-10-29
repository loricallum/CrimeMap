from django.test import TestCase

class CallsTest(TestCase):
    def test_map_call(self):
        response = self.client.get('', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'map_viewer/map.html')
