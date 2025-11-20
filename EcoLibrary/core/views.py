from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import evento as Evento
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    #return HttpResponse(titulo)
    return render(request,'core/home.html')
    
def events(request):
    events = Evento.objects.all().order_by('fecha')
    return render(request, 'core/events.html', {'eventos': events})

def community(request):
    #return HttpResponse(titulo)
    return render(request,'core/community.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def inscribirse_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if not evento.hay_cupo():
        messages.error(request, "Este evento ya está lleno.")
    elif request.user in evento.inscritos.all():
        messages.warning(request, "Ya estás inscrito en este evento.")
    else:
        evento.inscritos.add(request.user)
        messages.success(request, "Te has inscrito correctamente al evento.")
    return redirect('events')

@login_required
def desinscribirse_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.user in evento.inscritos.all():
        evento.inscritos.remove(request.user)
        messages.success(request, "Te has desinscrito del evento.")
    else:
        messages.warning(request, "No estabas inscrito en este evento.")
    
    next_url = request.POST.get('stay', 'events')
    return redirect(next_url)

@login_required
def mis_eventos(request):
    eventos_inscritos = Evento.objects.filter(inscritos=request.user).order_by('fecha')
    return render(request, 'core/user.html', {'eventos': eventos_inscritos})