from django import forms


class RegisterForm(forms.Form):
    email = forms.EmailField(
        max_length=24,
        label="email"
    )
    username = forms.CharField(
        max_length=16,
        label="username"
    )
    password = forms.CharField(
        label="password",
        max_length=16,
    )


class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=24,
        label="email"
    )

    password = forms.CharField(
        label="password",
        max_length=16,
    )