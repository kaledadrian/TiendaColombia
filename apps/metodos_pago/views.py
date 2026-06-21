from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import MetodoPago
from .forms import MetodoPagoForm
from apps.actores.decorators import admin_required


@admin_required
def lista_metodos(request):
    metodos = MetodoPago.objects.all().order_by('nombre')
    return render(request, 'metodos_pago/lista_metodos.html', {'metodos': metodos})


@admin_required
def crear_metodo(request):
    if request.method == 'POST':
        form = MetodoPagoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Método de pago creado exitosamente')
            return redirect('lista_metodos')
    else:
        form = MetodoPagoForm()
    return render(request, 'metodos_pago/crear_metodo.html', {'form': form})


@admin_required
def editar_metodo(request, id):
    metodo = get_object_or_404(MetodoPago, id=id)
    if request.method == 'POST':
        form = MetodoPagoForm(request.POST, instance=metodo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Método de pago actualizado exitosamente')
            return redirect('lista_metodos')
    else:
        form = MetodoPagoForm(instance=metodo)
    return render(request, 'metodos_pago/editar_metodo.html', {'form': form, 'metodo': metodo})


@admin_required
def eliminar_metodo(request, id):
    metodo = get_object_or_404(MetodoPago, id=id)
    if request.method == 'POST':
        metodo.delete()
        messages.success(request, 'Método de pago eliminado exitosamente')
        return redirect('lista_metodos')
    return render(request, 'metodos_pago/eliminar_metodo.html', {'metodo': metodo})
