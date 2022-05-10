from django.http import HttpResponse
from django.shortcuts import render, HttpResponse,redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Libro,Avatar
from .forms import LibroForm
from .forms import  RegistroUsuario, EditarUsuario,AvatarForm

def incio(request):
    return render(request,"principal/inicio.html")

def nosotros(request):
    return render(request,"principal/nosotros.html")


def libros(request):
    libros=Libro.objects.all()
    return render(request,"libros/index.html",{"libros":libros})

def crear(request):
    formulario=LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect("libros")
    return render(request,"libros/crear.html",{"formulario":formulario})

def editar(request,id):
    libro=Libro.objects.get(id=id)
    formulario=LibroForm(request.POST or None,request.FILES or None, instance=libro)
    if formulario.is_valid and request.POST:
        formulario.save()
        return redirect("libros")
    return render (request,"libros/editar.html",{"formulario":formulario})

def eliminar(request,id):
    libro=Libro.objects.get(id=id)
    libro.delete()
    return redirect ("libros")

def busquedaLibro(request):
    if request.GET.get('titulo'):
        titulo = request.GET.get('titulo')
        Libro= Libro.objects.filter(titulo__icontains=titulo)
        
        return render(request, 'libros/buscar_libro.html', {'titulo':titulo})
        
    else:
        respuesta = 'No hay datos para buscar'
        return render(request, 'libros/buscar_libro.html', {'respuesta':respuesta})
    


def login_req(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contra)
            
            if user is not None:
                login(request, user)
                return render(request, 'funciones/index.html', {'mensaje':'Te logueste con éxito!'})
            else:
                return render(request, 'funciones/login_fail.html', {'mensaje':'Error: Credenciales incorrectas', 'error':True})
        else:
            return render(request, 'funciones/login_fail.html', {'mensaje':'Error: Los datos tienen mal formato', 'error':True})
            
    form = AuthenticationForm()
    
    return render(request, 'funciones/login.html', {'form':form, 'mensaje':'', 'error':False})

def registro_req(request):
    if request.method == 'POST':
        form = RegistroUsuario(request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, 'funciones/index.html', {'tiene_mensaje': True, 'mensaje': f'Se creo el {usuario}'})
        
    form = RegistroUsuario()
    return render(request, 'funciones/registro.html', {'form': form, 'mensaje': '', 'error': False})

@login_required
def editar_usuario(request):
    usuario = request.user
    
    if request.method == 'POST':
        form = EditarUsuario(request.POST)
        
        if form.is_valid():
            datos = form.cleaned_data
            
            usuario.email = datos['email']
            usuario.password1 = datos['password1']
            usuario.password2 = datos['password2']
            usuario.first_name = datos['first_name']
            usuario.last_name = datos['last_name']
            
            usuario.save()
            
            return render(request, 'funcioens/index.html', {'tiene_mensaje':True, 'mensaje': f'Se edito correctamente'})
    else:
        form = EditarUsuario(initial={'first_name': usuario.first_name, 'last_name': usuario.last_name, 'email': usuario.email})
    
    return render(request, 'funciones/EditarPerfil.html', {'form': form})

@login_required
def info_usuario(request):  
    return render(request, 'funciones/info_usuario.html')

def login_fail(request):
    return render(request, 'funciones/login_fail.html')


def editar_avatar(request):
     usuario = request.user
    
     if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        
        if form.is_valid():
          avatar = Avatar.object.get(user=usuario)
          avatar.avatar = form.cleaned_data['avatar']
          avatar.save()
            
          return render(request, 'funciones/index.html',
                         {'tiene_mensaje':True, 'mensaje':f'Se cargo correctamente el avatar', 'url_avatar': avatar.avatar.url})
     else:
      form = AvatarForm()
    
      return render(request, 'funciones/editar_avatar.html', {'form':form})
   
            
        
 



