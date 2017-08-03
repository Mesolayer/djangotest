from django import forms
from .models import Friends

class InputForm(forms.ModelForm):
    class Meta:
        model = Friends
        exclude = ('',)
