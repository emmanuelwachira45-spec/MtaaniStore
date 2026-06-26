
from django.contrib import admin
from django.urls import path
from storeapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', views.home, name = 'home'),

    path('about/', views.about, name = 'about'),

    path('contact/', views.contact, name = 'contact'),

    path('gallery/', views.gallery, name = 'gallery'),

    path('services/', views.services, name = 'services'),

    path('lists/', views.lists, name = 'lists'),
]
