from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from proyecto3 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #Cada aplicacion maneja sus rutas (urls) 
    #En cada app creamos su urls y en el urls del proyecto ponemos los urls de las apps
    path('', include("aplicacion.urls")),
]
#Clase 24 - Para que tome los Avatars
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)