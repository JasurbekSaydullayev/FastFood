from rest_framework.permissions import BasePermission


class CanAccessObject(BasePermission):
    """
    Пользователь имеет доступ к объекту, если он является его владельцем или администратором.
    """

    def has_permission(self, request, view):
        return request.user or request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # Проверяем, является ли текущий пользователь владельцем объекта или администратором
        return obj == request.user or request.user.is_staff


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff