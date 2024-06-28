from rest_framework.generics import GenericAPIView,RetrieveUpdateDestroyAPIView, ListAPIView

from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


# Create your views here.


class CreateItemsView(GenericAPIView):
    serializer_class = CreateItemSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = self.request.user
        item_data=request.data
        item_data['user'] = user.id

        serializer = self.serializer_class(data=item_data, context={'user': user})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            item = serializer.data
            return Response({
                'message': f'Item {item["name"]} created successfully',
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ItemsView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ItemSerializer
    lookup_field='id'

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return ItemUpdateSerializer
        return ItemSerializer

    def get_queryset(self):
        return Item.objects.all()
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            self.perform_update(serializer)
            return Response({
                "msg": f"Item {instance.name} sucessfully updated"
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            self.perform_destroy(instance)
            return Response({
                "msg": f"Item {instance.name} sucessfully deleted"
            }, status=status.HTTP_200_OK)  


class ListItemsView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListItemSerializer
    queryset = Item.objects.all()