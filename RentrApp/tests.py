from django.core.urlresolvers import reverse
from setuptools.compat import unicode
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.

class RentableTestCase(APITestCase):

    # Tests creating a rentable with a POST
    def test_create_rentable(self):
        print("********************************************")
        print("Test the creation of a rentable using a POST")
        print("********************************************")
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
        print("Expected Status Code %s" % (status.HTTP_201_CREATED))
        print("Returned Status Code %s" % (response.status_code))
        self.assertEqual(response.data, data)
        print(response.data)

    # Negative test for creating a rentable
    def test_create_invalid_rentable(self):
        print("*****************************************************")
        print("Test the creation of an invalid rentable using a POST")
        print("*****************************************************")
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
        print("Expected Status Code %s" % (status.HTTP_400_BAD_REQUEST))
        print("Returned Status Code %s" % (response.status_code))

    # Using a GET returns a list of all objects
    def test_rentable_list(self):
        url = reverse('rentableList')
        print("***********************************")
        print("Test using a GET to get all objects")
        print("***********************************")
        for x in range(0, 5):
            data = {'store': None,
                'type': unicode('WaveRunner'),
                'isRented': True,
                'dateRented': unicode('2015-03-11T23:29:56.947000Z'),
                'dateDue': unicode('2015-03-11T23:29:56.947000Z'),
                'dateReturned': unicode('2015-03-11T23:29:56.947000Z'),
                'price': x}
            response = self.client.post(url, data, format='json')
        getResponse = self.client.get(url, format='json')
        print("Number of returned objects")
        print("Expected 5")
        print("Returned %s" % (len(getResponse.data)))
        self.assertEqual(len(getResponse.data), 5)

    # Using a Get when no rentables are saved returns an empty array
    def test_empty_rentable_list(self):
        url = reverse('rentableList')
        print("**********************************************")
        print("Test using a GET to get an empty rentable list")
        print("**********************************************")
        getResponse = self.client.get(url, format='json')
        print("Expected []")
        print("Returned %s" % (getResponse.data))
