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
    path(
        "montadoras/update/<str:pk>/", views.montadora_update, name="montadora_update"
    ),
    path("modelos/update/<str:pk>/", views.modelo_update, name="modelo_update"),
    path("veiculos/update/<str:pk>/", views.veiculo_update, name="veiculo_update"),
    path("modelos/list", views.modelo_list, name="modelo_list"),
    path("modelos/create", views.modelo_create, name="modelo_create"),
    path("modelos/delete/<str:pk>/", views.modelo_delete, name="modelo_delete"),
    path("modelos/detail/<str:pk>", views.modelo_detail, name="modelo_detail"),
    path("veiculos/list", views.veiculo_list, name="veiculo_list"),
    path("veiculos/create", views.veiculo_create, name="veiculo_create"),
    path("veiculos/delete/<str:pk>/", views.veiculo_delete, name="veiculo_delete"),
    path("veiculos/detail/<str:pk>/", views.veiculo_detail, name="veiculo_detail"),
]
