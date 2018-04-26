from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .models import Board,Category
from custom.models import Custom
# Create your views here.
class BoardHome(TemplateView):
    template_name = 'board/board_home.html'

    def get_context_data(self, **kwargs):
        cate = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context['cate'] = cate
        return context

def board_set_list(request):
    sets = Custom.objects.all()
    cate = Category.objects.all()
    return render(request, 'board/board_set_list.html',{'sets':sets,'cate':cate})

def board_list(request):
    ctgr = request.GET.get('category')
    if ctgr != None:
        boards = Board.objects.filter(category__name = ctgr)
    else:
        boards = Board.objects.all()
    cate = Category.objects.all()
    return render(request,'board/board_list.html',{'boards':boards,'cate':cate})

