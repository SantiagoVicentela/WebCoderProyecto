from django.urls import path
from . import views
from django.conf import settings 
from django.contrib.staticfiles.urls import static 
from django.contrib.auth.views import LogoutView


urlpatterns= [
   path("",views.incio,name="inicio"),
   path("nosotros",views.nosotros,name="nosotros"),
   path("libros",views.libros,name="libros"),
   path("libros/crear",views.crear,name="crear"), 
   path("libros/editar",views.editar,name="editar"),
   path("eliminar/<int:id>", views.eliminar,name="eliminar"),
   path("libros/editar/<int:id>", views.editar,name="editar"),
   path("login",views.login_req,name="login"),
   path("register",views.registro_req,name="register"),
   path("logout",LogoutView.as_view(template_name="libros/logout.html"), name="logout"),
   path('login_fail/', views.login_fail, name = 'login_fail'),
   path('editar_perfil/', views.editar_usuario, name = 'editar'),
   path('info_usuario/', views.info_usuario, name = 'info_usuario'),
   path('editar_avatar/', views.editar_avatar, name = 'editar_avatar')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)