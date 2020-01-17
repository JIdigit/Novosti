from django import forms
from django.contrib.auth.models import User
from .models import News, Comments

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']


class UserLogin(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)

class NewsCreateForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('category', 'title', 'image', 'body')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text', )


class LikeButtonForm(forms.Form):
    like = forms.BooleanField()