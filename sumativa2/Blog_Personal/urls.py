from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('', views.blog, name='blog'),
    path('publicacion/<int:publicacion_id>/', views.detalle_publicacion, name='detalle_publicacion'),
]