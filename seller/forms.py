from django import forms
from django.forms import TextInput, EmailInput, Select, DateInput
from django.utils import timezone

from seller.models import Seller


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['first_name', 'last_name', 'email', 'gender',
                  'birth_date', 'active']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'gender': Select(attrs={'class': 'form-select'}),
            'birth_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()  # Call the parent class's clean method

        # Retrieve the birth_date from cleaned_data
        birth_date = cleaned_data.get('birth_date')

        # Check if birth_date is provided and the user is at least 18 years old
        if birth_date:
            age = timezone.now().year - birth_date.year - (
                        (timezone.now().month, timezone.now().day) < (birth_date.month, birth_date.day))
            if age < 18:
                msg = 'Seller must be at least 18 years old.'
                self.add_error('birth_date', msg)

        # Check if the email is already used
        get_email = cleaned_data.get('email')
        if get_email:
            check_email = Seller.objects.filter(email=get_email)
            if check_email:
                msg = 'This email address is already used.'
                self.add_error('email', msg)



