from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from core.forms import AnoForm
from utils.checarAno.checarAno import verSeAnoEBissexto


def home(request):
    form = AnoForm(request.POST or None)

    context = {}
    context['form'] = form

    if request.method == "POST":
        try:
            if form.is_valid():
                ano = int(request.POST.get('ano'))
                context['eBissexto'] = verSeAnoEBissexto(ano)
                context['ano'] = ano

                return render(request, 'home.html', context)

        except (KeyError, Exception):
            context['errorMessage'] = 'Ocorreu um erro durante a submissão. Favor, tente novamente.'
            return render(request, 'home.html', context)
    return render(request, 'home.html', context)

