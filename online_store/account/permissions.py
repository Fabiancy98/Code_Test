from rest_framework.permissions import BasePermission





class IsEmployee(BasePermission):
    def has_permission(self, request, view):

        user = request.user
        if user.is_staff:
            return True
        return False
    
