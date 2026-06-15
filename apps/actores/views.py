from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Actor
from .forms import LoginForm, UsuarioForm
from .decorators import admin_required


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                usuario = Actor.objects.get(email=email, activo=True)
                if usuario.check_password(password):
                    request.session['usuario_id'] = usuario.id
                    request.session['usuario_nombre'] = usuario.nombre
                    request.session['rol'] = usuario.rol
                    messages.success(request, f'¡Bienvenido {usuario.nombre}!')
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Contraseña incorrecta')
            except Actor.DoesNotExist:
                messages.error(request, 'Usuario no encontrado o inactivo')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    request.session.flush()
    messages.success(request, 'Sesión cerrada correctamente')
    return redirect('login')


@admin_required
def lista_usuarios(request):
    usuarios = Actor.objects.all().order_by('-fecha_registro')
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})


@admin_required
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            password = form.cleaned_data.get('password')
            if password:
                usuario.set_password(password)
            usuario.save()
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()

    return render(request, 'usuarios/crear_usuario.html', {'form': form})


@admin_required
def editar_usuario(request, id):
    usuario = get_object_or_404(Actor, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            if password:
                user.set_password(password)
            user.save()
            messages.success(request, 'Usuario actualizado exitosamente')
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'usuarios/editar_usuario.html', {'form': form, 'usuario': usuario})


@admin_required
def eliminar_usuario(request, id):
    usuario = get_object_or_404(Actor, id=id)
    if request.method == 'POST':
        if usuario.id == request.session['usuario_id']:
            messages.error(request, 'No puedes eliminar tu propio usuario')
            return redirect('lista_usuarios')
        usuario.delete()
        messages.success(request, 'Usuario eliminado exitosamente')
        return redirect('lista_usuarios')

    return render(request, 'usuarios/eliminar_usuario.html', {'usuario': usuario})
