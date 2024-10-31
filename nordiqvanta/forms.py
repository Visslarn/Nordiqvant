from django import forms

class CVUploadForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    cv = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
