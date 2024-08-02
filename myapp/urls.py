from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('store_ip/', views.store_ip, name='store_ip'),
]
