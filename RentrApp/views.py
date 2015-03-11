from django.http import Http404
from RentrApp.serializers import RentableObjectSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

# Rental List
class RentableObjectList(APIView):

    # Returns a list of rentableObjects
    def get(self, request, format='json'):
        rentals = RentableObject.objects.all()
        serializer = RentableObjectSerializer(rentals, many=True)
        return Response(serializer.data)

    # Creates a new rentableObject
    def post(self, request, format='json'):
        serializer = RentableObjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RentableObjectDetail(APIView):

    # If object dosen't exsist throw a 404
    # Passes the rentableObject to the get function
    def get_object(self, pk):
        try:
            return RentableObject.objects.get(pk=pk)
        except RentableObject.DoesNotExist:
            raise Http404

    # Serializes the rentableObject and returns the individual rentableObject
    def get(self, request, pk, format='json'):
        rental = self.get_object(pk)
        serializer = RentableObjectSerializer(rental)
        return Response(serializer.data)

    # Updates the rentableObject when POST request
    def post(self, request, pk, format='json'):
        rental = self.get_object(pk)
        serializer = RentableObjectSerializer(rental, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)