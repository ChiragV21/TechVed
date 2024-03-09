from typing import Protocol
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.db.models.query_utils import Q
from .forms import CustomSetPasswordForm, CustomPasswordResetForm
from .decorators import user_not_authenticated
from .tokens import account_activation_token
from .forms import CustomRegisterForm

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(
            request,
            "Thank you for your email confirmation. Now you can login your account.",
        )
        return redirect("login")
    else:
        pass
        #messages.error(request, "Activation link is invalid!")
    return redirect("login")

def activateEmail(request, user, to_email):
    mail_subject = "Greenstaff US: Activate your user account."
    message = render_to_string(
        "template_activate_account.html",
        {
            "user": user.username,
            "domain": get_current_site(request).domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": account_activation_token.make_token(user),
            "protocol": "https" if request.is_secure() else "http",
        },
    )
    email = EmailMessage(mail_subject, message, to=[to_email])
    if  email.send():
        messages.success(
            request,
            f"Dear {user}, please go to you email {to_email} inbox and click on received activation link to confirm and complete the registration. Note: If you have not seen email in inbox, Please Check your spam folder.",
        )
    else:
        messages.error(
            request,
            f"Problem sending confirmation email to {to_email}, check if you typed it correctly.",
        )


# Create your views here.
def Registration(request):
    if request.method == "POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            form_user = register_form.save(commit=False)
            form_user.username = register_form.cleaned_data.get('email')
            form_user.is_active = False
            form_user.save()
            activateEmail(request, form_user, register_form.cleaned_data.get("email"))
            return redirect("Registration")
        else:
            messages.error(request, ("You have not regesitered, Please check.."))
    else:
        register_form = CustomRegisterForm()

    return render(
        request=request,
        template_name="register.html",
        context={"register_form": register_form},
    )

@login_required
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = CustomSetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, "Your password has been changed")
            return redirect('Homepage')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect('password_change')

    form = CustomSetPasswordForm(user)
    return render(request, 'password_reset_confirm.html', {'form': form})

@user_not_authenticated
def password_reset_request(request):
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = get_user_model().objects.filter(Q(email=user_email)).first()
            
            if associated_user is None:
                messages.error(request, "This email does not exist.")
                return redirect('password_reset')
            
            if associated_user:
                subject = "Password Reset request"
                message = render_to_string("template_reset_password.html", {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'token': account_activation_token.make_token(associated_user),
                    "protocol": 'https' if request.is_secure() else 'http'
                })
                email = EmailMessage(subject, message, to=[associated_user.email])
                if email.send():
                    messages.success(request,
                        """ Password reset sent.
                            We've emailed you instructions for setting your password, if an account exists with the email you entered. 
                            You should receive them shortly.If you don't receive an email, please make sure you've entered the address 
                            you registered with, and check your spam folder.
                        """
                    )
                else:
                    messages.error(request, "Problem sending reset password email, <b>SERVER PROBLEM</b>")
            return redirect('login')

    form = CustomPasswordResetForm()
    return render(
        request=request, 
        template_name="password_reset.html", 
        context={"form": form}
        )

def passwordResetConfirm(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = CustomSetPasswordForm(user, request.POST)
            if form.is_valid():
                new_password = form.cleaned_data['new_password2']
                if user.check_password(new_password):  # Check if new password is the same as the old one
                    messages.error(request, "Your new password must be different from your previous password.")
                    return redirect('password_reset_confirm', uidb64=uidb64, token=token)
                else:
                    user.set_password(new_password)
                    user.save()
                    messages.success(request, "Your password has been set. You may go ahead and log in now.")
                    return redirect('login')
            else:
                for error in list(form.errors.values()):  
                    messages.error(request, error)

        form = CustomSetPasswordForm(user)
        return render(request, 'password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, "Link is expired")

    messages.error(request, 'Something went wrong, redirecting back to Homepage')
    return redirect("Homepage")