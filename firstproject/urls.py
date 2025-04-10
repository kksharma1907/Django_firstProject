from django.contrib import admin
from django.urls import path
from web.views import index, home, contact, about, login, create_employee  # ✅ Import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('home/', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('employee/', create_employee, name='employee'),
    path('login/', login, name='login'),  
]
