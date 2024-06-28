from django.urls import path
from .views import *

urlpatterns = [
    path('item/create/', CreateItemsView.as_view(), name='create-item'),
    path('item/list/', ListItemsView.as_view(), name='list-items'),
    path('item/<int:id>/', ItemsView.as_view(), name='get-item'),
]
