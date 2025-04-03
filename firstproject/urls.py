from django.contrib import admin
from django.urls import path
from web.views import index, home, contact, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('contact/', contact, name='contact'), 
    path('about/', about, name='about'),
]
