from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import libro as Libro
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .services import get_book_extra_data

def book_detail_view(request, isbn):
    libro = get_object_or_404(Libro, isbn=isbn)
    extra = get_book_extra_data(libro.isbn)

    return render(request, "core/book_detail.html", {
        "book": libro,
        "extra": extra,
    })

def home(request):
    #return HttpResponse(titulo)
    return render(request,'core/home.html')
    
def books(request):
    libro = Libro.objects.all().order_by('titulo')
    return render(request, 'core/books.html', {'libros': libro})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Cuenta creada.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def anadir_favoritos(request, libro_id):
    # Busca el libro en la coleccion
    libro = get_object_or_404(Libro, id=libro_id)
    # Revisa si el usuario ya tiene el libro en sus favoritos
    # Si lo está, no hace nada
    if request.user in libro.favoritos.all():
        messages.warning(request, "Ya está en favoritos.")
    # Si no, lo añade
    else:
        libro.favoritos.add(request.user)
        messages.success(request, "Añadido a favoritos.")
    return redirect('books')

@login_required
def quitar_favoritos(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    # Revisa si el libro ya está en favoritos
    # Si lo está, lo quita
    if request.user in libro.favoritos.all():
        libro.favoritos.remove(request.user)
        messages.success(request, "Libro quitado de favoritos.")
    # Si no, no hace nada
    else:
        messages.warning(request, "No estaba entre tus favoritos.")
    
    next_url = request.POST.get('stay', 'books')
    return redirect(next_url)

@login_required
def mis_favoritos(request):
    libros_favoritos = Libro.objects.filter(inscritos=request.user).order_by('titulo')
    return render(request, 'core/user.html', {'libros': libros_favoritos})