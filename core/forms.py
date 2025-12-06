from django import forms
from django.core.validators import FileExtensionValidator

class EncodeForm(forms.Form):
    image = forms.ImageField(label='Select Image', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}), label='Secret Message')
    password = forms.CharField(widget=forms.PasswordInput, label='Password', required=True)

class DecodeForm(forms.Form):
    image = forms.ImageField(label='Select Image to Decode', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    password = forms.CharField(widget=forms.PasswordInput, label='Password', required=True)
