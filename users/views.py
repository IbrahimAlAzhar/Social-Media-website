from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm  # when you use built in form then import this
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm  # in forms.py here create a UserRegistration form


def register(request):
    if request.method == 'POST':   # when value is post,then it is works
        # form = UserCreationForm(request.POST), create automatically a django built in form and stores in form variable
        form = UserRegisterForm(request.POST)   # in forms.py there create manually a form
        if form.is_valid():   # if there has alreday has a username or password does not match than it is not valid
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'You account has been created! You are able to log in!') # here using flash message, which shows one time and then disappear and link on to base.html
            return redirect('login')     # the blog/views.home is naming by blog-home
    else:                                 # now redirect to login page
        form = UserRegisterForm  # there django provides a built in an empty form
    return render(request,'users/register.html', {'form':form})


@login_required     # for checking whether the user is logged in now to show the profile
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)   # here those variables for update
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)  # this parameters works for current user information
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()  # user form and profile form save if those are valid
            p_form.save()
            messages.success(request,f'Your account has been updated!')  # here this message shows one time
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'users/profile.html',context)

# the function is used for: when we apply profile option without login then the page redirect to login then after the login the page go to profile

