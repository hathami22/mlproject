from django.contrib import admin
from django.urls import path, include
from PublicpriveApp.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),                 # page d’accueil
    path('', include('PublicpriveApp.urls')),    # inclut /predict/


]
