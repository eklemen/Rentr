from django.http import Http404
from RentrApp.models import Rentable, Store
from RentrApp.serializers import RentableSerializer, StoreSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

# Rental List
class RentableList(APIView):

    # Returns a list of rentables
    def get(self, request, format='json'):
        store = request.GET.get('store')
        if store != None:
            rentals = Rentable.objects.all(store=store)
        else:
            rentals = Rentable.objects.all()
        serializer = RentableSerializer(rentals, many=True)
        return Response(serializer.data)

    # Creates a new rentable
    def post(self, request, format='json'):
        serializer = RentableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RentableDetail(APIView):

    # If object dosen't exsist throw a 404
    # Passes the rentable to the get function
    def get_object(self, pk, format='json'):
        try:
            return Rentable.objects.get(pk=pk)
        except Rentable.DoesNotExist:
            raise Http404

    # Serializes the rentable and returns the individual rentable
    def get(self, request, pk, format='json'):
        rental = self.get_object(pk)
        serializer = RentableSerializer(rental)
        return Response(serializer.data)

    # Updates the rentableObject when POST request
    def post(self, request, pk, format='json'):
        rental = self.get_object(pk)
        serializer = RentableSerializer(rental, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StoreDetail(APIView):

    def get_object(self, pk, format='json'):
        try:
            return Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            raise Http404

    def get(self, request, pk, format='json'):
        store = self.get_object(pk)
        serializer = StoreSerializer(store)
        return Response(serializer.data)