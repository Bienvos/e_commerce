"""
URL configuration for SRI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from univ import views
#from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.connexion,name='login'),
    #path('news', views.requette,name='nouveau'),
    path('teste', views.test,name='tester'),
    path('ajouter', views.fr,name='formulaire'),
    path('<int:id>/', views.update,name='updata'),
    path('supprimer/<int:id>', views.supprimer,name='supprime'),
    path('registre', views.registrer,name='registre'),
    path('login', views.connexion,name='login'),
    path('securite',views.pers, name='securite'),
    path('logout', views.deconnexion,name='logout'),
    path('reservation', views.reser,name='reservation'),
    path('confirmation',views.confirmation,name='confirmation'),
    

   ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
