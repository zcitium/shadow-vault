from django import forms
from django.core.validators import FileExtensionValidator

class EncodeForm(forms.Form):
    image = forms.ImageField(label='Select Image', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}), label='Secret Message')
    password = forms.CharField(widget=forms.PasswordInput, label='Password', required=True)

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if not image.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                raise forms.ValidationError("Only PNG and JPG files are allowed.")
            if image.size > 2 * 1024 * 1024: # 2MB Strict Limit for Input (prevents bloating > 4.5MB)
                raise forms.ValidationError("Image file too large (> 2MB). Please compress it.")
        return image

class DecodeForm(forms.Form):
    image = forms.ImageField(label='Select Image to Decode', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    password = forms.CharField(widget=forms.PasswordInput, label='Password', required=True)

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if not image.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                raise forms.ValidationError("Only PNG and JPG files are allowed.")
            if image.size > 4.5 * 1024 * 1024: # 4.5MB Hard Limit for Decrypt
                raise forms.ValidationError("Image file too large ( > 4.5MB).")
        return image
