from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied


def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('usuario_id'):
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper


def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('usuario_id'):
            return redirect('login')
        if request.session.get('rol') != 'admin':
            raise PermissionDenied("No tienes permisos de administrador")
        return view_func(request, *args, **kwargs)
    return wrapper
