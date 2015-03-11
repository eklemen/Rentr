from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.

class RentableObjectTestCase(APITestCase):

    # Tests creating a rentableObject with a POST
    def test_create_rentable_oject(self):
        url = reverse('rentableObjectList')
        data = {'': ''}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)