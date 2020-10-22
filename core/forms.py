from django.forms import ModelForm, TextInput, Textarea
from core.models import Remember


class RememberForm(ModelForm):
    """Form for adding a new memory"""
    class Meta:
        model = Remember
        widgets = {
            'remember': Textarea(attrs={'class': 'form-control'}),
        }
        fields = ['remember', 'coordinate']
