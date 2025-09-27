from django.shortcuts import render, redirect, get_object_or_404
from .models import Transacao
from .forms import TransacaoForm
# Create your views here.


def home(request):
    return render(request, 'contas/home.html')


def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)


def nova_transacao(request):
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    return render(request, 'contas/form.html', {'form': form})


def update(request, pk):
    transacao = get_object_or_404(Transacao, pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    return render(request, 'contas/form.html', {'form': form, 'transacao': transacao})


def delete(request, pk):
    transacao = get_object_or_404(Transacao, pk=pk)
    transacao.delete()
    return redirect('url_listagem')