from rest_framework import serializers
from .models import *
from inventory.models import Item

class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'created_at', 'updated_at']

class SupplierDetailsSerializer(serializers.ModelSerializer):
    items = ItemDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Supplier
        fields = ['id', 'name', 'email', 'phone_number', 'address', 'items']


class SupplierListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = ['id', 'name', 'email']


class CreateSupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = ['name', 'email', 'phone_number', 'address']

    def create(self, validated_data):
        supplier = Supplier.objects.create( **validated_data)
        return supplier