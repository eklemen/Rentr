from rest_framework import serializers
from RentrApp.models import Rentable, Store

class RentableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rentable
        fields = ('store', 'type', 'isRented', 'dateRented', 'dateDue', 'dateReturned',)

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('name', 'address', 'isRented', 'phoneNum')
