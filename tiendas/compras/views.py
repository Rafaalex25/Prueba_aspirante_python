from django.shortcuts import render,redirect
from .models import *
from .forms import *



def Home(request, template_name="templates/formulario.html"):
    if request.method == 'POST':
        form = FormularioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return redirect('Home')
    else:
        form = FormularioForm()
    return render(request, template_name, locals(), )
