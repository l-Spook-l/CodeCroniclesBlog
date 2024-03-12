from rest_framework import permissions


class OnlyAuthorPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # "Allow GET, HEAD, or OPTIONS requests (safe requests)"
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the current user is the owner of the object
        return obj.author == request.user
