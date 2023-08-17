from django import forms


class Signup_Form(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=100)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}), max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), max_length=100)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), max_length=100)


