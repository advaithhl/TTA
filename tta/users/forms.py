from django import forms
from .models import Passenger
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    age = forms.IntegerField(min_value=18)
    gender = forms.ChoiceField(
        choices=Passenger.GENDER_CHOICES, widget=forms.RadioSelect)
    address = forms.CharField(max_length=300)
    email = forms.EmailField()
    phone_no = forms.CharField(label='Phone number')

    class Meta:
        model = Passenger
        fields = ['first_name', 'last_name', 'age', 'gender', 'address',
                  'phone_no', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        self.instance.first_name = self.cleaned_data.get('first_name')
        self.instance.last_name = self.cleaned_data.get('last_name')
        self.instance.age = self.cleaned_data.get('age')
        self.instance.gender = self.cleaned_data.get('gender')
        self.instance.address = self.cleaned_data.get('address')
        self.instance.phone_no = self.cleaned_data.get('phone_no')
        super(UserRegisterForm, self).save(commit=commit)


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    age = forms.IntegerField(min_value=18)
    gender = forms.ChoiceField(
        choices=Passenger.GENDER_CHOICES, widget=forms.RadioSelect)
    address = forms.CharField(max_length=300)
    email = forms.EmailField()
    phone_no = forms.CharField(label='Phone number')

    class Meta:
        model = Passenger
        fields = ['first_name', 'last_name', 'age', 'gender', 'address',
                  'phone_no', 'username', 'email']
