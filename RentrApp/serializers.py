from rest_framework import serializers

class RentableObjectSerializer(serializers.Serializer):
    class Meta:
        model = RentableObjectSerializer
        fields = ('store', 'type', 'isRented', 'dateRented', 'dateDue', 'dateReturned', 'price')

class StoreSerializer(serializers.Serializer):
    class Meta:
        model = StoreSerializer
        fields = ('name', 'address', 'isRented', 'phoneNum')