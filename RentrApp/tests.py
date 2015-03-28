import json
from django.core.urlresolvers import reverse
from setuptools.compat import unicode
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here

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
                'dateReturned': unicode('2015-03-11T23:29:56.947000Z'),}
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
                'dateReturned': '',}
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
                'dateReturned': unicode('2015-03-11T23:29:56.947000Z'),}
            self.client.post(url, data, format='json')
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

class RentableDetailTestCase(APITestCase):

    def test_get_rentable_detail(self):
        print("***************************************************")
        print("Test using a GET to get a rentable by a specific pk")
        print("***************************************************")
        createUrl = reverse('rentableList')
        data = {'store': None,
                'type': unicode('WaveRunner'),
                'isRented': True,
                'dateRented': unicode('2015-03-11T23:29:56.947000Z'),
                'dateDue': unicode('2015-03-11T23:29:56.947000Z'),
                'dateReturned': unicode('2015-03-11T23:29:56.947000Z'),}
        postResponse = self.client.post(createUrl, data, format='json')
        getResponse = self.client.get('/rentable/?pk=1', format='json')
        print("Expected: %s" % (postResponse.data))
        print("Returned: %s" % (getResponse.data[0]))
        self.assertEqual(getResponse.data[0], postResponse.data)

    def test_get_invalid_rentable(self):
        print("*******************************************************")
        print("Test using a GET to get a 404 when no rentable is found")
        print("*******************************************************")
        url = reverse('rentable', args='5')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print("Expected Status Code %s" % (status.HTTP_404_NOT_FOUND))
        print("Returned Status Code %s" % (response.status_code))
        
        
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
                'dateReturned': unicode('2015-03-11T23:29:56.947000Z'),} 
        response = self.client.post(url, data, format='json')
        # Now edit the data
        url = reverse('rentable', args='1')
        data['isRented'] = False
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("Expected Status Code %s" % (status.HTTP_200_OK))
        print("Returned Status Code %s" % (response.status_code))
        self.assertEqual(response.data, data)
        print(response.data)



class StoreDetailTestCase(APITestCase):
    
    def test_get_invalid_store(self):
        print("*******************************************************")
        print("Test using a GET to get a 404 when no store is found")
        print("*******************************************************")
        getResponse = self.client.get('/store/?pk=5', format='json')
        self.assertEqual(getResponse.status_code, status.HTTP_404_NOT_FOUND, msg="Expecting a 404 Error")





 
