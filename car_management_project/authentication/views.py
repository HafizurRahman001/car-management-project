from django.shortcuts import render
from authentication.forms import SignUpForm, ChangeUserData
from django.shortcuts import render,redirect
from django.contrib import messages
from view_details.models import Purchase
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy

# Create your views here.
def user_signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, "Account created successfully")
            return redirect('login')
    else:
        signup_form = SignUpForm()
    return render(request,'login_signin_form.html', {'form':signup_form, 'type': 'Register'})



# login using class based loginview
class UserLogIn(LoginView):
    template_name = 'login_signin_form.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, "User Loged in successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, "User Loged in information incorrect")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    

def user_logout(request):
    logout(request)
    messages.success(request, "User Loged out successfully")
    return redirect('login')
    



def profile(request):
    return render(request,'profile.html')


@login_required(login_url="/authentication/login/")
def update_profile(request):
        if request.method == 'POST':
            profile_form = ChangeUserData(request.POST, instance=request.user)
            if profile_form.is_valid():
                print(profile_form.cleaned_data)
                profile_form.save()
                messages.success(request, "Your Profile updated successfully")
                return redirect('profile')
        else:
            profile_form = ChangeUserData(instance=request.user)
        return render(request,'login_signin_form.html', {'form':profile_form, 'type': 'Update profile'})




@login_required(login_url="/authentication/login/")
def password_change(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, data = request.POST)
        if password_change_form.is_valid():
            password_change_form.save()
            update_session_auth_hash(request,password_change_form.user)
            messages.success(request, "Yor Password updated successfully")
            return redirect('profile')
    else:
        password_change_form = PasswordChangeForm(user=request.user)
    return render(request,'login_signin_form.html', {'form':password_change_form, 'type': 'Password-change'})




@login_required(login_url="/authentication/login/")
def display_purchase_history(request):
    purchases = Purchase.objects.filter(author=request.user)
    purchased_products = []

    for data in purchases:
        product = data.product
        purchased_products.append(product)

    return render(request,'profile.html', {'purchaseData': purchased_products})
