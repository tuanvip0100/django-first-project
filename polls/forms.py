from django import forms


class NameForm(forms.Form):
    user_name = forms.CharField(label='User name', max_length=100)


class LoginForm(forms.Form):
    user_name = forms.CharField(label='User name', max_length=200)
    password = forms.CharField(label='Password', max_length=50)


class ChangeName(forms.Form):
    user_name = forms.CharField(label='User name', max_length=200)


class SignIn(forms.Form):
    user_name = forms.CharField(label='User name', max_length=200)
    password = forms.CharField(label='Password', max_length=50)
    email = forms.CharField(label='email', max_length=100)
    age = forms.IntegerField(label='age',max_value=200)
