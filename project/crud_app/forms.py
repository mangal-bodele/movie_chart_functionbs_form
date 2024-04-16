from django import forms
from .models import Moviechart

class MoviechartForm(forms.ModelForm):
    class Meta:
        model = Moviechart
        fields = '__all__'