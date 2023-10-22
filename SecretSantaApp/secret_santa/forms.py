from django import forms
from .models import Name, Rule

class NameForm(forms.ModelForm):
    class Meta:
        model = Name
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter a name'}),
        }

class RuleForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields = ['name1', 'name2']
