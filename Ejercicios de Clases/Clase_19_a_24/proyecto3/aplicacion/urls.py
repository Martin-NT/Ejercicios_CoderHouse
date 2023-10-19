from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    #Cada aplicacion maneja sus rutas (urls) 
    #En cada app creamos su urls y en el urls del proyecto ponemos los urls de las apps
    # Rutas propias de la aplicacion 
    path('', home, name="home" ),
    path('cursos/', cursos, name="cursos" ),
    path('estudiantes2/', estudiantes2, name="estudiantes2" ),
    path('entregables/', entregables, name="entregables" ),
    
    path('curso_form/', cursoForm, name="curso_form" ),
    path('curso_form2/', cursoForm2, name="curso_form2" ),
    
    path('buscar_curso/', buscarCurso, name="buscar_curso" ),
    path('buscar2/', buscar2, name="buscar2" ),

#----------------------- Clase 22 - Playground avanzado parte I -----------------------
    path('profesores/', profesores, name="profesores" ),
    path('update_profesor/<id_profesor>/', updateProfesor, name="update_profesor" ),
    path('delete_profesor/<id_profesor>/', deleteProfesor, name="delete_profesor" ),
    path('create_profesor/', createProfesor, name="create_profesor" ),

    path('estudiantes/', EstudianteList.as_view(), name="estudiantes" ),
    path('create_estudiante/', EstudianteCreate.as_view(), name="create_estudiante" ),    
    path('update_estudiante/<int:pk>/', EstudianteUpdate.as_view(), name="update_estudiante" ),
    path('delete_estudiante/<int:pk>/', EstudianteDelete.as_view(), name="delete_estudiante" ),

#----------------------- Clase 23 - Playground avanzado parte II -----------------------
    path('login/', login_request, name="login" ),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout" ),
    path('registro/', register, name="registro" ),

#----------------------- Clase 24 - Playground avanzado parte III -----------------------
    path('editar_perfil/', editarPerfil, name="editar_perfil" ),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar" ),
]

