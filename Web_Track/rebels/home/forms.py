from django import forms

from .models import Score

class FileForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = [
            'source_file',
            'description'
        ]
