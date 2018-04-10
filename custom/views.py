from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *
from .forms import *

# Create your views here.
# 함수형 view
def custom_new(request):
    hardware = Hardware.objects.all()
    compa = Compa.objects.all()
    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            hard = form.save(commit=False)
            hard.user = request.user
            hard.save()
            return redirect('custom:customdetail', pk=hard.pk)
    else:
        form = CustomForm()

    return render(request, 'custom/custom_edit.html',{'form':form,'hards':hardware,'compa':compa})

def custom_edit(request, pk):
    hard = get_object_or_404(Custom, pk)
    if request.method == 'POST':
        form = CustomForm(request.POST, instance=hard)
        if form.is_valid():
            hard = form.save(commit=False)



# 클래스형 view
class CustomListView(ListView):
    model = Custom
    template_name = 'custom/custom_list.html'

class CustomDetailView(DetailView):
    model = Custom
    template_name = 'custom/custom_detail.html'



