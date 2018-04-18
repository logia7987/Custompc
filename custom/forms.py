from django import forms
from .models import *

class CustomForm(forms.ModelForm):

    class Meta:
        model = Custom
        fields = ('cpu','board','ram','vga','power','hdd','ssd','odd','text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)