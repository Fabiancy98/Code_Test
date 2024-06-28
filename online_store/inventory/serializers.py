from rest_framework import serializers
from .models import *
from suppliers.models import Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'email', 'phone_number', 'address']

class ItemSerializer(serializers.ModelSerializer):
    suppliers = SupplierSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'created_at', 'updated_at','suppliers']

class ListItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price']


class CreateItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['id', 'user', 'name', 'description', 'price', 'suppliers']


    def validate(self, attrs):
        price= attrs.get('price')
        if price is not None and price < 0.00 :
            raise serializers.ValidationError("Invalid price")
        return super().validate(attrs)


    def create(self, validated_data):
        suppliers_data = validated_data.pop('suppliers', [])
        item = Item.objects.create(**validated_data)
        item.suppliers.set(suppliers_data)
        return item

class ItemUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'suppliers']


    def validate(self, attrs):
        price= attrs.get('price')
        if price is not None and price < 0.00 :
            raise serializers.ValidationError("Invalid price")
        return super().validate(attrs)


    def update(self, instance, validated_data):
        suppliers = validated_data.pop('suppliers', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if suppliers is not None:
            instance.suppliers.set(suppliers)
        instance.save()
        return instance
