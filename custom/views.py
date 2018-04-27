from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView, CreateView
from .models import *
from .forms import *
# 함수형 view

def custom_detail(request, pk):
    set = get_object_or_404(Custom, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.custom = set
            comment.author = request.user
            comment.save()
    else:
        form = CommentForm()

    return render(request, 'custom/custom_detail.html',{'set':set,'form':form})

def custom_new(request):
    cpu = Hardware.objects.filter(hardware_kind="CPU")[:10]
    board = Hardware.objects.filter(hardware_kind="BRD")[:10]
    ram = Hardware.objects.filter(hardware_kind="RAM")[:10]
    vga = Hardware.objects.filter(hardware_kind="VGA")[:10]
    power = Hardware.objects.filter(hardware_kind="POW")[:10]
    hdd = Hardware.objects.filter(hardware_kind="HDD")[:10]
    ssd = Hardware.objects.filter(hardware_kind="SSD")[:10]
    odd = Hardware.objects.filter(hardware_kind="ODD")[:10]
    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            hard = form.save(commit=False)
            hard.user = request.user
            hard.save()
            return redirect('custom:custom_detail', pk=hard.pk)
    else:
        form = CustomForm()

    return render(request, 'custom/custom_new.html',{'form':form,'cpu':cpu,'board':board,'ram':ram,'vga':vga,'power':power,'hdd':hdd,'ssd':ssd,'odd':odd})

def custom_edit(request, pk):
    cpu = Hardware.objects.filter(hardware_kind="CPU")[:10]
    board = Hardware.objects.filter(hardware_kind="BRD")[:10]
    ram = Hardware.objects.filter(hardware_kind="RAM")[:10]
    vga = Hardware.objects.filter(hardware_kind="VGA")[:10]
    power = Hardware.objects.filter(hardware_kind="POW")[:10]
    hdd = Hardware.objects.filter(hardware_kind="HDD")[:10]
    ssd = Hardware.objects.filter(hardware_kind="SSD")[:10]
    odd = Hardware.objects.filter(hardware_kind="ODD")[:10]
    hard = get_object_or_404(Custom, pk=pk)
    if request.method == 'POST':
        form = CustomForm(request.POST, instance=hard)
        if form.is_valid():
            hard = form.save(commit=False)
            hard.user = request.user
            hard.save()
            return redirect('custom:custom_detail', pk=hard.pk)
    else:
        form = CustomUpdateForm(instance=hard)

    return render(request, 'custom/custom_new.html', {'form': form, 'hard': hard,'cpu':cpu,'board':board,'ram':ram,'vga':vga,'power':power,'hdd':hdd,'ssd':ssd,'odd':odd})

def custom_detail(request, pk):
    set = get_object_or_404(Custom, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.custom = set
            comment.author = request.user
            comment.save()
            return redirect('custom:custom_detail', pk=set.pk)
    else:
        form = CommentForm()

    return render(request, 'custom/custom_detail.html',{'set':set,'form':form})

def comment_remove(request,pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('custom:custom_detail', pk=comment.custom.pk)

# 클래스형 view
class CustomDeleteView(DeleteView):
    model = Custom
    template_name = 'custom/custom_delete.html'
    success_url = reverse_lazy('board:board_set_list')