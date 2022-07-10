from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('tour/<int:id>', views.tour, name='tour'),
    path('success', views.request_form, name='success')
]