from django import forms
from paths.models import FieldModel

class FieldForm(forms.ModelForm):
    class Meta:
        model = FieldModel
        fields = ['FieldTitle','FieldDescription','image']