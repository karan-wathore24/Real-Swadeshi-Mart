from django.contrib.auth.forms import UserCreationForm
from .models import User


class SellerRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_seller = True
        user.is_customer = False
        if commit:
            user.save()
        return user


class CustomerRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        user.is_seller = False
        if commit:
            user.save()
        return user
