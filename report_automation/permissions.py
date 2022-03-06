from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        if view.action == 'list':
            return request.user.is_staff or request.user.groups.filter(name='teachers').exists()
        elif view.action == 'create':
            return request.user.is_superuser
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False
                                                                                                
    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False

        if view.action == 'retrieve':
            return obj == request.user or request.user.is_staff
        elif view.action in ['update', 'partial_update']:
            return obj == request.user or request.user.is_staff
        elif view.action == 'destroy':
            return request.user.is_staff
        else:
            return False



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



class GradePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.groups.filter(name='teachers').exists() or request.user.is_staff
        elif view.action == 'retrieve':
            return request.user.groups.filter(name='students').exists() or request.user.groups.filter(name='teachers').exists() or request.user.is_staff
        else:
            return False
                                                                                                
    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False
        if view.action == 'list':
            return request.user.groups.filter(name='students').exists() or request.user.groups.filter(name='teachers').exists() or request.user.is_staff
        if view.action == 'retrieve':
            return  obj.student == request.user or request.user.groups.filter(name='teachers').exists() or request.user.is_staff
        else:
            return False