from django import forms
from django.contrib.auth.forms import UserCreationForm

# models
from accounts.models import User
from accounts.models import Profile
from accounts.models import Address


# Widgets
from accounts.widgets import CustomPictureImageFieldWidget


# forms
class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)

class ClientSignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2','is_client','is_staff',)


class ProfileForm(forms.ModelForm):
    photo = forms.ImageField(widget=CustomPictureImageFieldWidget)

    class Meta:
        model = Profile
        exclude = ('user',)


class PresentAddressForm(forms.ModelForm):

    class Meta:
        model = Address
        exclude = ('address_of',)
