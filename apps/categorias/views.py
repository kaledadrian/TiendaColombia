from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Categoria
from .forms import CategoriaForm
from apps.actores.decorators import admin_required


@admin_required
def lista_categorias(request):
    categorias = Categoria.objects.all().order_by('nombre')
    return render(request, 'categorias/lista_categorias.html', {'categorias': categorias})


@admin_required
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada exitosamente')
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()

    return render(request, 'categorias/crear_categoria.html', {'form': form})


@admin_required
def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada exitosamente')
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'categorias/editar_categoria.html', {'form': form, 'categoria': categoria})


@admin_required
def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoría eliminada exitosamente')
        return redirect('lista_categorias')

    return render(request, 'categorias/eliminar_categoria.html', {'categoria': categoria})
