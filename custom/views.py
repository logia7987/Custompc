from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import *
from .forms import *

# Create your views here.
def custom_edit(request):
    hardware = Hardware.objects.all()
    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            hard = form.save(commit=False)
            hard.user = request.user
            hard.save()
            return redirect()
    else:
        form = CustomForm()

    return render(request, 'custom/custom_edit.html',{'form':form,'hards':hardware})




