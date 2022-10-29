from django.test import TestCase
from common.models import Crime
from .police_api_service import save_crimes_JSON

class PoliceApiTest(TestCase):
    def test_get_all_crimes(self):
        
        expectedJSON=[{"category": "anti-social-behaviour", "location_type": "Force", "location": {"latitude": "51.995788", "street": {"id": 709710, "name": "On or near Willow Bank Road"}, "longitude": "-2.002983"}, "context": "", "outcome_status": None, "persistent_id": "ad6bfcbfca5afde180645a6d86d80a0e90485e0285469db80a294d307a229a0f", "id": 74001629, "location_subtype": "", "month": "2019-05"}]
        response = self.client.get('/api/getallcrimes?lat=52&lng=-2&date=2019-05')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, expectedJSON)

    def test_save_crimes_JSON(self):
        crimes=[{"category": "anti-social-behaviour", "location_type": "Force", "location": {"latitude": "51.995788", "street": {"id": 709710, "name": "On or near Willow Bank Road"}, "longitude": "-2.002983"}, "context": "", "outcome_status": None, "persistent_id": "ad6bfcbfca5afde180645a6d86d80a0e90485e0285469db80a294d307a229a0f", "id": 74001629, "location_subtype": "", "month": "2019-05"}]
        
        expectedCrimes = save_crimes_JSON(crimes)
        actualCrimes = list(Crime.objects.all())

        self.assertListEqual(expectedCrimes, actualCrimes)
        


