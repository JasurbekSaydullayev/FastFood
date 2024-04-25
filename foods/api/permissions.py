from rest_framework.permissions import BasePermission


class IsWaitressOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if not request.user:
            return False
        return request.user and request.user.type == "Waitress" or request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff
