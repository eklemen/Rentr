from rest_framework import serializers
from RentrApp.models import RentableObject, Store

class RentableObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentableObject
        fields = ('store', 'type', 'isRented', 'dateRented', 'dateDue', 'dateReturned', 'price')

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('name', 'address', 'isRented', 'phoneNum')
