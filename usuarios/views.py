from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta {username} Creada Exitosamente!')
            return redirect('inicio-sesion')
    else:
        form = UserRegisterForm()
    return render(request, 'usuarios/registro.html', {'form':form})

def inicio(request):
    return render(request, 'usuarios/inicio_sesion.html')
