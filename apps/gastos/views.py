from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Count, Q
from django.contrib import messages
from datetime import datetime, timedelta
from decimal import Decimal
from .models import Gasto
from .forms import GastoForm, FiltroGastosForm
from apps.actores.models import Actor
from apps.actores.decorators import login_required


@login_required
def dashboard(request):
    usuario_id = request.session.get('usuario_id')
    usuario = Actor.objects.get(id=usuario_id)

    if usuario.rol == 'admin':
        gastos = Gasto.objects.all()
    else:
        gastos = Gasto.objects.filter(usuario=usuario)

    total_gastos = gastos.aggregate(total=Sum('monto'))['total'] or 0

    ultimo_mes = datetime.now().date() - timedelta(days=30)
    gastos_30dias = gastos.filter(fecha__gte=ultimo_mes)
    total_30dias = gastos_30dias.aggregate(total=Sum('monto'))['total'] or 0

    gastos_por_categoria = list(gastos.values('categoria__nombre', 'categoria__color').annotate(
        total=Sum('monto'),
        cantidad=Count('id')
    ).order_by('-total')[:5])

    hoy = datetime.now().date()
    nombres_meses = {
        1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril',
        5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto',
        9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
    }
    meses = []
    for i in range(5, -1, -1):
        fecha = hoy.replace(day=1) - timedelta(days=30 * i)
        mes_num = fecha.month
        anio_num = fecha.year
        mes_nombre = f"{nombres_meses[mes_num]} {anio_num}"
        gastos_mes = gastos.filter(fecha__year=anio_num, fecha__month=mes_num)
        total_mes = gastos_mes.aggregate(total=Sum('monto'))['total'] or 0
        meses.append({'nombre': mes_nombre, 'total': float(total_mes)})

    ultimos_gastos = gastos[:10]

    context = {
        'usuario': usuario,
        'total_gastos': float(total_gastos),
        'total_30dias': float(total_30dias),
        'gastos_por_categoria': gastos_por_categoria,
        'gastos_mensuales': meses,
        'ultimos_gastos': ultimos_gastos,
        'cantidad_gastos': gastos.count(),
    }
    return render(request, 'dashboard.html', context)


@login_required
def lista_gastos(request):
    usuario_id = request.session.get('usuario_id')
    usuario = Actor.objects.get(id=usuario_id)

    if usuario.rol == 'admin':
        gastos = Gasto.objects.all()
    else:
        gastos = Gasto.objects.filter(usuario=usuario)

    form = FiltroGastosForm(request.GET)
    if form.is_valid():
        fecha_desde = form.cleaned_data.get('fecha_desde')
        fecha_hasta = form.cleaned_data.get('fecha_hasta')
        categoria = form.cleaned_data.get('categoria')
        busqueda = form.cleaned_data.get('busqueda')

        if fecha_desde:
            gastos = gastos.filter(fecha__gte=fecha_desde)
        if fecha_hasta:
            gastos = gastos.filter(fecha__lte=fecha_hasta)
        if categoria:
            gastos = gastos.filter(categoria=categoria)
        if busqueda:
            gastos = gastos.filter(
                Q(titulo__icontains=busqueda) |
                Q(descripcion__icontains=busqueda)
            )

    total = gastos.aggregate(total=Sum('monto'))['total'] or Decimal('0')
    gastos = gastos.order_by('-fecha')

    context = {
        'gastos': gastos,
        'form': form,
        'usuario': usuario,
        'total': total,
    }
    return render(request, 'gastos/lista_gastos.html', context)


@login_required
def crear_gasto(request):
    if request.method == 'POST':
        form = GastoForm(request.POST, request.FILES)
        if form.is_valid():
            gasto = form.save(commit=False)
            gasto.usuario = Actor.objects.get(id=request.session['usuario_id'])
            gasto.save()
            messages.success(request, 'Gasto creado exitosamente')
            return redirect('lista_gastos')
    else:
        form = GastoForm()

    return render(request, 'gastos/crear_gasto.html', {'form': form})


@login_required
def editar_gasto(request, id):
    gasto = get_object_or_404(Gasto, id=id)
    usuario = Actor.objects.get(id=request.session['usuario_id'])

    if usuario.rol != 'admin' and gasto.usuario.id != usuario.id:
        messages.error(request, 'No tienes permiso para editar este gasto')
        return redirect('lista_gastos')

    if request.method == 'POST':
        form = GastoForm(request.POST, request.FILES, instance=gasto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gasto actualizado exitosamente')
            return redirect('lista_gastos')
    else:
        form = GastoForm(instance=gasto)

    return render(request, 'gastos/editar_gasto.html', {'form': form, 'gasto': gasto})


@login_required
def eliminar_gasto(request, id):
    gasto = get_object_or_404(Gasto, id=id)
    usuario = Actor.objects.get(id=request.session['usuario_id'])

    if usuario.rol != 'admin' and gasto.usuario.id != usuario.id:
        messages.error(request, 'No tienes permiso para eliminar este gasto')
        return redirect('lista_gastos')

    if request.method == 'POST':
        gasto.delete()
        messages.success(request, 'Gasto eliminado exitosamente')
        return redirect('lista_gastos')

    return render(request, 'gastos/eliminar_gasto.html', {'gasto': gasto})


@login_required
def reportes(request):
    usuario_id = request.session.get('usuario_id')
    usuario = Actor.objects.get(id=usuario_id)

    if usuario.rol == 'admin':
        gastos = Gasto.objects.all()
    else:
        gastos = Gasto.objects.filter(usuario=usuario)

    fecha_desde = request.GET.get('fecha_desde')
    fecha_hasta = request.GET.get('fecha_hasta')

    if fecha_desde and fecha_hasta:
        gastos = gastos.filter(fecha__gte=fecha_desde, fecha__lte=fecha_hasta)

    reporte_categorias = gastos.values('categoria__nombre', 'categoria__color').annotate(
        total=Sum('monto'),
        cantidad=Count('id')
    ).order_by('-total')

    reporte_mensual = gastos.values('fecha__year', 'fecha__month').annotate(
        total=Sum('monto'),
        cantidad=Count('id')
    ).order_by('fecha__year', 'fecha__month')

    meses_es = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio',
                7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}

    for item in reporte_mensual:
        item['nombre_mes'] = f"{meses_es[item['fecha__month']]} {item['fecha__year']}"

    total_general = gastos.aggregate(total=Sum('monto'))['total'] or 0

    context = {
        'reporte_categorias': reporte_categorias,
        'reporte_mensual': reporte_mensual,
        'total_general': float(total_general),
        'fecha_desde': fecha_desde,
        'fecha_hasta': fecha_hasta,
        'usuario': usuario,
    }
    return render(request, 'reportes/reportes.html', context)
