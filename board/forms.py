from django import forms
from .models import Board, BoardComment

class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ('title','category','text')

class BoardCommentForm(forms.ModelForm):
    class Meta:
        model = BoardComment
        fields = ('text',)