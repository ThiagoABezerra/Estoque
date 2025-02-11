from django.contrib import admin
from Estoque.models import Epi, Produto, Usuario, Departamento

class EpiAdmin(admin.ModelAdmin):
    list_display = ('name', 'ca','tamanho')
    search_fields = ('name',)
admin.site.register(Epi, EpiAdmin)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantidade','medida','peso')
    search_fields = ('name',)
admin.site.register(Produto, ProdutoAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('name', 'departamento','cargo','centro_custo')
    search_fields = ('name',)
admin.site.register(Usuario, UsuarioAdmin)

class departamentoAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
admin.site.register(Departamento, departamentoAdmin)
