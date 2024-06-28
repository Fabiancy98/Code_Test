from django.urls import path
from .views import *

urlpatterns = [
    path('supplier/create/', CreateSupplierView.as_view(), name='create-supplier'),
    path('supplier/list/', GetSupplierListView.as_view(), name='list-suppliers'),
    path('supplier/<int:id>/', SupplierView.as_view(), name='get-supplier'),
]
