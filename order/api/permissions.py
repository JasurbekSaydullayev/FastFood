from rest_framework import permissions


class CustomerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff or request.user.type == 'customer'


class WaitressOrCourierOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.type != "Customer"


class WaitressOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff or request.user.type == 'waitress'


class CanObjectAccess(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff or request.user.type == 'customer'

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class CourierOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff or request.user.type == 'Courier'
