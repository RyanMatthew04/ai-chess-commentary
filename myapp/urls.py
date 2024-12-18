from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('start_commentary/', views.start_commentary_view, name='start_commentary'),
    path('stop_commentary/', views.stop_commentary_view, name='stop_commentary'),
]
