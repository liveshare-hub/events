from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .models import PesertaEvent
from .forms import CreateUserForm

def createUser(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Akun {username} Berhasil di Buat')
        messages.error(request, f'Registrasi Gagal! Silahkan coba lagi!')
    form = CreateUserForm()
    return render(request, 'accounts/register.html',{'form':form})

def loginUser(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Selamat Datang {username}')
                
                return redirect('home')

            else:
                messages.error(request, f'Periksa kembali user anda!')
    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    messages.info(request, f'Akun berhasil logout')
    return redirect('login')            
