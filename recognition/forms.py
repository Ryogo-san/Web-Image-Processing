from django import forms
from .models import InputImage


class InputImageForm(forms.ModelForm):
    """
    画像フォームを定義
    """
    class Meta:
        model = InputImage
        fields = ("image",)
