from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from .models import Board,Category,BoardComment
from .forms import BoardForm,BoardCommentForm
from custom.models import Custom
# Create your views here.
class BoardHome(TemplateView):
    template_name = 'board/board_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cate'] = Category.objects.all()[:10]
        context['board'] = Board.objects.all()[:10]
        context['custom'] = Custom.objects.all()[:10]
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
    return render(request,'board/board_list.html',{'boards':boards,'cate':cate,'ctgr':ctgr})

def board_detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    cate = Category.objects.all()
    if request.method == 'POST':
        form = BoardCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.board = board
            comment.author = request.user
            comment.save()
            return redirect('board:board_detail', pk=board.pk)
    else:
        form = BoardCommentForm()

    return render(request, 'board/board_detail.html',{'board':board,'cate':cate,'form':form})

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
    return render(request, 'board/board_edit.html',{'form':form,'cate':cate})

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
    return render(request, 'board/board_edit.html',{'form':form,'cate':cate})

def board_remove(request, pk):
    board = get_object_or_404(Board, pk=pk)
    board.delete()
    return redirect('board:board_list')

def board_comment_remove(request, pk):
    comment = get_object_or_404(BoardComment, pk=pk)
    comment.delete()
    return redirect('board:board_detail', pk=comment.board.pk)