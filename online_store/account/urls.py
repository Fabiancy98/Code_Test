from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserview.as_view(), name='logout'),
    path('profile/employee/<str:id>', EditEmployeeProfileView.as_view(), name='edit-employee'),
]
