from rest_framework import permissions


class OnlyAuthorPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Разрешить GET, HEAD или OPTIONS запросы (безопасные запросы)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Проверить, является ли текущий пользователь владельцем объекта
        return obj.author == request.user
