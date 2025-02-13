from django.contrib import admin
from django.urls import path
from controle.views import epi_view, new_epi_view, excluir_epi, EpiUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('epis/', epi_view, name ='epis_list'),
    path('new_epi/', new_epi_view, name ='new_epi'),
    path('excluir_epi/<int:id>/excluir/', excluir_epi, name='excluir_epi'),
    path('editar_epi/<int:pk>/update/', EpiUpdateView.as_view(), name='editar_epi'),
]
