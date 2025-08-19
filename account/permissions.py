from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'admin'


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type in ['admin', 'staff']


class IsClient(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'client'