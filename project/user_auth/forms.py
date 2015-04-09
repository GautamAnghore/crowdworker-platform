from django import forms


class SignUpForm(forms.Form):

    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', max_length=50)
    name = forms.CharField(label='name', max_length=200)
    email = forms.EmailField(label='email', max_length=200)
    country = forms.CharField(label='country', max_length=50)
    phone = forms.IntegerField(label='phone')
    about = forms.CharField(widget=forms.Textarea(attrs={'title': 'About'}))
