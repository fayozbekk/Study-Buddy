from django.forms import ModelForm, TextInput, Textarea, CharField
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RoomForm(ModelForm):
    class Meta:
        model = RoomModel
        fields = ['title', 'content', 'category']
        widgets = {
            'title': TextInput(attrs={
                'class': 'inpt',
                'placeholder': 'Title'
            }),
            'content': Textarea(attrs={
                'class': 'inpt',
                'placeholder': 'Content'
            })

        }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['cat_name']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': TextInput(attrs={
                'class': "inpt",
                'placeholder': 'Username'
            }),
            'password': TextInput(attrs={
                'class': "inpt",
                'placeholder': 'Password',
                'type': 'password'
            })
        }


class CustomUserForm(UserCreationForm):
    password1 = CharField(widget=TextInput(attrs={
        'class': 'inpt',
        'type': 'password',
        'placeholder': 'Enter your password'
    }))
    password2 = CharField(widget=TextInput(attrs={
        'class': 'inpt',
        'type': 'password',
        'placeholder': 'Confirm your password'
    }))


class Meta:
    model = User
    fields = ['username',
              'first_name',
              'last_name',
              'avatar',
              'bio',
              'email',
              'password1',
              'password2']
    widgets = {
        'username': TextInput(attrs={
            'class': "inpt",
            'placeholder': 'Username'
        }),
        'first_name': TextInput(attrs={
            'class': "inpt",
            'placeholder': 'First name',
        }),
        'last_name': TextInput(attrs={
            'class': "inpt",
            'placeholder': 'last name',
        }),
        'bio': Textarea(attrs={
            'class': 'input',
            'rows': '4',
            'cols': '50'
        }),
        'email': TextInput(attrs={
            'class': 'inpt',
            'placeholder': 'E-mail',
        }),
        'password1': TextInput(attrs={
            'class': 'inpt',
            'placeholder': 'Enter your password',

        })
    }


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['message']
        widgets = {
            'message': TextInput(attrs={
                'class': 'inpt',
                'placeholder': 'Enter your message🐬'
            })
        }
