from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.index, name='home'),
    path('infos/', views.infos, name='infos'),
    path('notes/', views.notes, name='notes'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about_us, name='about')
]