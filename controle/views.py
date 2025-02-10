from django.shortcuts import render, redirect, get_object_or_404
from controle.models import Epi
from controle.forms import EpiFrom
from django.contrib import messages


def epi_view(request):
     epis = Epi.objects.all().order_by('name')
     search = request.GET.get('search')

     if search:
          epis = epis.filter(name__icontains=search)
          
     return render(request, 'listar_epis.html', {'epis': epis})       


def new_epi_view(request):
     if request.method == 'POST':
         new_epi_from = EpiFrom(request.POST)
         if new_epi_from.is_valid():
               new_epi_from.save()          
               return redirect('epis_list')         
     else:
         new_epi_from = EpiFrom()
     return render(request, 'new_epi.html', {'new_epi_from': new_epi_from})    
    
def excluir_epi(request, id):
    epi_excluir = get_object_or_404(Epi, id=id)
    if request.method == 'POST':
        epi_excluir.delete()
        messages.success(request, f'O item "{Epi.name}" foi excluído com sucesso!')
        return redirect('epis_list')
    return render(request, 'confirmar_exclusao_epi.html', {'epi_excluir': epi_excluir})