
from django.contrib import admin
from django.urls import path
from myApp.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('', about_list, name='about_list'),

    
    path('create/', about_create, name='about_create'),

    path('update/<int:id>/',about_update, name='about_update'),
    path('delete/<int:id>/', about_delete, name='about_delete'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
