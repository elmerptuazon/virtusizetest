from django.urls import path, include
from .views import index, addLink, getAll

urlpatterns = [
    path('count/', index),
    path('store/link/', addLink),
    path('view/link/<id>/', getAll),
]
