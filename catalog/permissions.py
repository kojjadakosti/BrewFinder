from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminUserOrReadOnly(BasePermission):
    """
    Разрешает доступ только для админов (на запись), остальным только чтение.
    """

    def has_permission(self, request, view):
        # Чтение — разрешено всем
        if request.method in SAFE_METHODS:
            return True

        # Только админам можно что-то менять
        return request.user and request.user.is_authenticated and request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        # Чтение — всем
        if request.method in SAFE_METHODS:
            return True

        # Изменения только для админов
        return request.user and request.user.is_superuser


class IsBreweryOwnerOrAdmin(BasePermission):
    """
    Только владелец пивоварни (при создании пива) или админ имеет доступ на запись.
    """

    def has_permission(self, request, view):
        # Разрешаем все безопасные методы
        if request.method in SAFE_METHODS:
            return True

        # Для небезопасных методов — только суперюзер или владелец пивоварни
        return request.user and (
                request.user.is_authenticated and (request.user.is_superuser or request.user.is_brewery_owner))

    def has_object_permission(self, request, view, obj):
        # Чтение — всем
        if request.method in SAFE_METHODS:
            return True

        # Редактировать может владелец пивоварни или админ
        return request.user.is_superuser or obj.brewery.owner == request.user
