from django.shortcuts import render, redirect, get_object_or_404
from .models import Bolo
from .forms import BoloForm


def pagina_inicial(request):
    return render(request, 'catalogo/index.html')


def lista_bolos(request):
    bolos = Bolo.objects.all()
    return render(request, 'catalogo/lista_bolos.html', {'bolos': bolos})


def detalhe_bolo(request, pk):
    bolo = get_object_or_404(Bolo, pk=pk)
    return render(request, 'catalogo/detalhe_bolo.html', {'bolo': bolo})


def novo_bolo(request):
    if request.method == 'POST':
        form = BoloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo:lista_bolos')
    else:
        form = BoloForm()

    return render(request, 'catalogo/bolo_form.html', {'form': form, 'titulo': 'Adicionar Novo Bolo'})


def editar_bolo(request, pk):
    bolo = get_object_or_404(Bolo, pk=pk)

    if request.method == 'POST':
        form = BoloForm(request.POST, instance=bolo)
        if form.is_valid():
            form.save()
            return redirect('catalogo:detalhe_bolo', pk=bolo.pk)
    else:
        form = BoloForm(instance=bolo)

    return render(request, 'catalogo/bolo_form.html', {'form': form, 'titulo': 'Editar Bolo', 'bolo': bolo})


def apagar_bolo(request, pk):
    bolo = get_object_or_404(Bolo, pk=pk)

    if request.method == 'POST':
        bolo.delete()
        return redirect('catalogo:lista_bolos')

    return render(request, 'catalogo/confirmar_exclusao.html', {'bolo': bolo})
