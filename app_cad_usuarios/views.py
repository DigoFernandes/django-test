from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':  # Verifica se o método HTTP é POST
        novo_usuario = Usuario()
        novo_usuario.username = request.POST.get('username')
        novo_usuario.password = request.POST.get('password')
        novo_usuario.save()  # Corrigido aqui: Adicionado parênteses ao método save()

    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', usuarios)