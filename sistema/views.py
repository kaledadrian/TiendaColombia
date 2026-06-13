from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Count, Q
from django.contrib import messages
from datetime import datetime, timedelta
from calendar import month_name
from decimal import Decimal
from .models import Actor, Categoria, MetodoPago, Gasto
from .forms import LoginForm, GastoForm, CategoriaForm, UsuarioForm, FiltroGastosForm
from .decorators import login_required, admin_required

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

@login_required
def dashboard(request):
    usuario_id = request.session.get('usuario_id')
    usuario = Actor.objects.get(id=usuario_id)
    
    # Filtrar gastos según rol
    if usuario.rol == 'admin':
        gastos = Gasto.objects.all()
    else:
        gastos = Gasto.objects.filter(usuario=usuario)
    
    # Totales generales
    total_gastos = gastos.aggregate(total=Sum('monto'))['total'] or 0
    
    # Gastos últimos 30 días
    ultimo_mes = datetime.now().date() - timedelta(days=30)
    gastos_30dias = gastos.filter(fecha__gte=ultimo_mes)
    total_30dias = gastos_30dias.aggregate(total=Sum('monto'))['total'] or 0
    
    # Gastos por categoría (Top 5)
    gastos_por_categoria = list(gastos.values('categoria__nombre', 'categoria__color').annotate(
        total=Sum('monto'),
        cantidad=Count('id')
    ).order_by('-total')[:5])
    
    # Gastos por mes (últimos 6 meses)
    hoy = datetime.now().date()
    meses = []
    
    for i in range(5, -1, -1):
        # Calcular fecha del mes
        fecha = hoy.replace(day=1) - timedelta(days=30*i)
        mes_num = fecha.month
        año_num = fecha.year
        
        # Obtener nombre del mes en español
        nombres_meses = {
            1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril',
            5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto',
            9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
        }
        mes_nombre = f"{nombres_meses[mes_num]} {año_num}"
        
        # Calcular total del mes
        gastos_mes = gastos.filter(fecha__year=año_num, fecha__month=mes_num)
        total_mes = gastos_mes.aggregate(total=Sum('monto'))['total'] or 0
        
        meses.append({
            'nombre': mes_nombre,
            'total': float(total_mes)
        })
    
    # Últimos 10 gastos
    ultimos_gastos = gastos[:10]
    
    # Imprimir en consola para depuración
    print("=== DATOS DEL GRÁFICO ===")
    for mes in meses:
        print(f"{mes['nombre']}: ${mes['total']:,.0f}")
    
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
    
    # Base de gastos según rol
    if usuario.rol == 'admin':
        gastos = Gasto.objects.all()
    else:
        gastos = Gasto.objects.filter(usuario=usuario)
    
    # Aplicar filtros
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
    
    # Calcular el total (IMPORTANTE: hacerlo después de los filtros)
    total = gastos.aggregate(total=Sum('monto'))['total'] or Decimal('0')
    
    # Ordenar por fecha más reciente
    gastos = gastos.order_by('-fecha')
    
    context = {
        'gastos': gastos,
        'form': form,
        'usuario': usuario,
        'total': total,  # ← PASAR EL TOTAL AL TEMPLATE
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

@login_required
def reportes(request):
    usuario_id = request.session.get('usuario_id')
    usuario = Actor.objects.get(id=usuario_id)
    
    if usuario.rol == 'admin':
        gastos = Gasto.objects.all()
    else:
        gastos = Gasto.objects.filter(usuario=usuario)
    
    # Filtros
    fecha_desde = request.GET.get('fecha_desde')
    fecha_hasta = request.GET.get('fecha_hasta')
    
    if fecha_desde and fecha_hasta:
        gastos = gastos.filter(fecha__gte=fecha_desde, fecha__lte=fecha_hasta)
    
    # Reporte por categoría
    reporte_categorias = gastos.values('categoria__nombre', 'categoria__color').annotate(
        total=Sum('monto'),
        cantidad=Count('id')
    ).order_by('-total')
    
    # Reporte mensual
    reporte_mensual = gastos.values('fecha__year', 'fecha__month').annotate(
        total=Sum('monto'),
        cantidad=Count('id')
    ).order_by('fecha__year', 'fecha__month')
    
    meses_es = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio',
                7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}
    
    for item in reporte_mensual:
        item['nombre_mes'] = f"{meses_es[item['fecha__month']]} {item['fecha__year']}"
    
    # Total general
    total_general = gastos.aggregate(total=Sum('monto'))['total'] or 0
    
    context = {
        'reporte_categorias': reporte_categorias,
        'reporte_mensual': reporte_mensual,
        'total_general': float(total_general),
        'fecha_desde': fecha_desde,
        'fecha_hasta': fecha_hasta,
        'usuario': usuario
    }
    return render(request, 'reportes/reportes.html', context)