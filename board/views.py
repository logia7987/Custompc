from django.shortcuts import render, get_object_or_404, redirect
from django.core import serializers
from django.http import JsonResponse
from django.views.generic import TemplateView
from .models import Board,Category
from .forms import BoardForm
from custom.forms import CommentForm
from custom.models import Custom, User
from django.contrib.auth.decorators import login_required
# Create your views here.
class BoardHome(TemplateView):
    template_name = 'board/board_home.html'

    def get_context_data(self, **kwargs):
        context = super(BoardHome, self).get_context_data(**kwargs)
        context['custom'] = Custom.objects.all().order_by('-create_date')[:10]
        context['ctgrs'] = Category.objects.all()
        context['boards'] = Board.objects.all().order_by('-created_date')
        return context

def board_set_list(request):
    sets = Custom.objects.all()
    ctgrs = Category.objects.all()
    return render(request, 'board/board_set_list.html',{'sets':sets,'ctgrs':ctgrs})

def board_list(request):
    ctgr = request.GET.get('category')
    if ctgr != None:
        boards = Board.objects.filter(category__name = ctgr)
    else:
        boards = Board.objects.all()
    ctgrs = Category.objects.all()
    return render(request,'board/board_list.html',{'boards':boards,'ctgrs':ctgrs,'ctgr':ctgr})

def board_detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    cate = Category.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.board = board
            comment.author = request.user
            comment.save()
            return redirect('board:board_detail', pk=board.pk)
    else:
        form = CommentForm()

    return render(request, 'board/board_detail.html',{'board':board,'ctgrs':cate,'form':form})

@login_required
def board_new(request):
    cate = Category.objects.all()
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.author = request.user
            board.save()
            return redirect('board:board_detail', pk=board.pk)
    else:
        form = BoardForm()
    return render(request, 'board/board_edit.html',{'form':form,'ctgrs':cate})

def board_edit(request, pk):
    board = get_object_or_404(Board, pk=pk)
    cate = Category.objects.all()
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.author = request.user
            board.save()
            return redirect('board:board_detail', pk=board.pk)
    else:
        form = BoardForm(instance=board)
    return render(request, 'board/board_edit.html',{'form':form,'ctgrs':cate})

def board_remove(request, pk):
    board = get_object_or_404(Board, pk=pk)
    board.delete()
    return redirect('board:board_home')

def board_list_data(request):
    sets = serializers.serialize('json', Custom.objects.all())
    boards = serializers.serialize('json', Board.objects.all())
    ctgrname = serializers.serialize('json', Category.objects.all())
    id = serializers.serialize('json', User.objects.all())
    data = {
        'sets':sets,
        'boards':boards,
        'id':id,
        'ctgrname':ctgrname
    }
    return JsonResponse(data)