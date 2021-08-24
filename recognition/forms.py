from django import forms
from .models import Prediction

class PredictionForm(forms.ModelForm):
    """
    画像フォームを定義
    """
    class Meta:
        model=Prediction
        fields=("image",)
