from django import forms 
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class CustomRegisterForm(UserCreationForm):
    first_name= forms.CharField()
    last_name= forms.CharField()
    email= forms.EmailField()
    # captcha=CaptchaField()
    class Meta:
        model= User 
        fields=['first_name','last_name','email','password1','password2']
        
    def is_valid(self) -> bool:
        valid = super().is_valid()
        if valid:
            email = self.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                self.add_error('email', 'This email is already associated with an existing account.')
                valid = False
        return valid
    
class CustomSetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']
    
class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)