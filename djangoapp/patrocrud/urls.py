from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("montadoras/list/", views.montadora_list, name="montadora_list"),
    path("montadoras/create/", views.montadora_create, name="montadora_create"),
    path("montadoras/detail/<str:pk>", views.montadora_detail, name="montadora_detail"),
    path(
        "montadoras/delete/<str:pk>/", views.montadora_delete, name="montadora_delete"
    ),
    path("modelos/list", views.modelo_list, name="modelo_list"),
    path("modelos/create", views.modelo_create, name="modelo_create"),
    path("modelos/delete/<str:pk>/", views.modelo_delete, name="modelo_delete"),
]
