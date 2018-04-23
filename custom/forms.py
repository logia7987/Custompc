from django import forms
from .models import *

class CustomForm(forms.ModelForm):

    class Meta:
        model = Custom
        fields = ('cpu','board','ram','vga','power','hdd','ssd','odd','text',)

class CustomUpdateForm(forms.Form,forms.ModelForm):
    # cpu = forms.ChoiceField(widget=forms.Select)
    # board = forms.ChoiceField(widget=forms.Select)
    # ram = forms.ChoiceField(widget=forms.Select)
    # vga = forms.ChoiceField(widget=forms.Select)
    # power = forms.ChoiceField(widget=forms.Select)
    # hdd = forms.ChoiceField(widget=forms.Select)
    # ssd = forms.ChoiceField(widget=forms.Select)
    # odd = forms.ChoiceField(widget=forms.Select)
    # text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Custom
        fields = ('cpu','board','ram','vga','power','hdd','ssd','odd','text')
        widgets = {
            'cpu':forms.HiddenInput(),
            'board':forms.HiddenInput(),
            'ram':forms.HiddenInput(),
            'vga':forms.HiddenInput(),
            'power':forms.HiddenInput(),
            'hdd':forms.HiddenInput(),
            'ssd':forms.HiddenInput(),
            'odd':forms.HiddenInput(),
            'text':forms.HiddenInput(),
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)