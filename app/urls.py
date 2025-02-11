from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Estoque.views import epi_view, new_epi_view, excluir_epi


urlpatterns = [
    path('admin/', admin.site.urls),
    path('epis/', epi_view, name ='epis_list'),
    path('new_epi/', new_epi_view, name ='new_epi'),
    path('excluir_epi/<int:id>/excluir/', excluir_epi, name='excluir_epi')

]
