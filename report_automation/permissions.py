from rest_framework import permissions


class ReportPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.groups.filter(name='students').exists() or request.user.groups.filter(name='teachers').exists() or request.user.is_staff
        elif view.action == 'create':
            return request.user.groups.filter(name='students').exists()
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False
                                                                                                
    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False
       
        if view.action == 'retrieve':
            return request.user.groups.filter(name='students').exists() or request.user.groups.filter(name='teachers').exists() or request.user.is_staff
        elif view.action in ['update', 'partial_update']:
            return obj.student == request.user
        elif view.action == 'destroy':
            return obj.student == request.user
        else:
            return False
