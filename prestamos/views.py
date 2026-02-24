from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Prestamo
from .forms import PrestamoForm
from libros.models import Libro

def lista_prestamos(request):
    prestamos = Prestamo.objects.all().order_by('-fecha_prestamo')
    form = PrestamoForm()
    return render(request, 'prestamos/lista.html', {'prestamos': prestamos, 'form': form})

def crear_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save(commit=False)
            libro = prestamo.libro

            if libro.stock > 0:
                libro.stock -= 1
                libro.save()
                prestamo.save()

    return redirect('lista_prestamos')

def devolver_libro(request, id):
    prestamo = get_object_or_404(Prestamo, id=id)

    if not prestamo.devuelto:
        prestamo.devuelto = True
        prestamo.fecha_devolucion = timezone.now().date()
        prestamo.save()

        libro = prestamo.libro
        libro.stock += 1
        libro.save()

    return redirect('lista_prestamos')