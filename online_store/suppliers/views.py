from rest_framework.generics import GenericAPIView,RetrieveUpdateDestroyAPIView, ListAPIView

from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


# Create your views here.


class CreateSupplierView(GenericAPIView):
    serializer_class = CreateSupplierSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        supply_data=request.data

        serializer = self.serializer_class(data=supply_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            supply = serializer.data
            return Response({
                'message': f'Supplier {supply["name"]} created successfully',
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SupplierView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SupplierDetailsSerializer
    lookup_field='id'

    def get_queryset(self):
        return Supplier.objects.all()
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            self.perform_update(serializer)
            return Response({
                "msg": f"Supplier {instance.name} sucessfully updated"
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            self.perform_destroy(instance)
            return Response({
                "msg": f"Supplier {instance.name} sucessfully deleted"
            }, status=status.HTTP_200_OK)  


class GetSupplierListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SupplierListSerializer
    
    def get_queryset(self):
        return Supplier.objects.all()
    