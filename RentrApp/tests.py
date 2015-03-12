from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import datetime
import json

# Create your tests here.

class RentableTestCase(APITestCase):

    # Tests creating a rentable with a POST
    def test_create_rentable(self):
        url = reverse('rentableList')
        data = {'store': None,
                'type': unicode('WaveRunner'),
                'isRented': True,
                'dateRented': unicode('2015-03-11T23:29:56.947000Z'),  
                'dateDue': unicode('2015-03-11T23:29:56.947000Z'),     
                'dateReturned': unicode('2015-03-11T23:29:56.947000Z'), 
                'price': 50.00}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)

    # Negative test for creating a rentable
    def test_create_invalid_rentable(self):
        url = reverse('rentableList')
        data = {'store': '',
                'type': '',
                'isRented': '',
                'dateRented': '',
                'dateDue': '',
                'dateReturned': '',
                'price': ''}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

