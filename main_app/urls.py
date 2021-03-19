from django.urls import path
from . import views 

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('', views.index, name='index'),
    path('cats/', views.cats_index, name='cats')
]