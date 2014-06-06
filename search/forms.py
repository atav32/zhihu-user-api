from django import forms
from djangular.forms import NgModelFormMixin

class SearchForm(forms.Form):
    search = forms.CharField(min_length=1, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username', 'required':'', 'autofocus':''}))
