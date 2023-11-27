from django import forms
from .models import FieldModel

class FieldForm(forms.ModelForm):
    class Meta:
        model = FieldModel
        fields = ['FieldTitle', 'FieldDescription', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add Tailwind CSS classes to form fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'w-full border p-2 my-2'

        # Example: Add placeholder text for the 'FieldTitle' field
        self.fields['FieldTitle'].widget.attrs['placeholder'] = 'Enter Field Title'
