from app1.forms import Signup_Form
from app1.models import Custom_user
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
import time

# Create your views here.

@never_cache
def loginpage(request):
    if 'username' in request.session:
        username = request.session['username']
        user = Custom_user.objects.get(username = username)

        if user.is_superuser:
            return redirect('adminHome')
        else:
            return redirect('userHome')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Custom_user.objects.get(username=username, password=password)

            if user is not None:
                if not user.is_superuser:
                    request.session['username'] = username
                    return redirect('userHome')
                else:
                    return render(request, 'loginpage.html', {'user404': 'Please use admin login'})

        except Custom_user.DoesNotExist:
            return render(request, 'loginpage.html', {'user404': 'Username or Password incorrect'})

    return render(request, 'loginpage.html')

def signup(request):
    form = Signup_Form()
    if request.method == 'POST':
        form = Signup_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['first_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            cpassword = form.cleaned_data['confirm_password']
            form = Signup_Form()
            if password == cpassword:
                if Custom_user.objects.filter(username = username).exists():
                    return render(request, 'signup.html',{ 'form': form,'pw_error': 'username already exist'})

                if Custom_user.objects.filter(email = email).exists():
                    return render(request, 'signup.html', {'form': form,'taken': 'Email already registered' })
                else:
                    Custom_user(first_name=name, username=username,password=password, email=email).save()
                    return render(request, 'signup.html', {'form': form,'taken': 'Signup Success'})

            else:
                return render(request, 'signup.html', {'form': form,'taken': 'Passwords do not match'})
        # else:
        #     return render(request, 'signup.html', {'form': form})
    else:
        form = Signup_Form()
    return render(request, 'signup.html', {'form': form})


def add_user(request):
    form = Signup_Form()
    if request.method == 'POST':
        # pDict = request.POST.copy()
        form = Signup_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['first_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            cpassword = form.cleaned_data['confirm_password']
            form = Signup_Form()
            if password == cpassword:
                if Custom_user.objects.filter(username = username).exists():
                    return render(request, 'add_user.html',{ 'form': form,'pw_error': 'username already exist'})

                if Custom_user.objects.filter(email = email).exists():
                    return render(request, 'add_user.html', {'form': form,'taken': 'Email already registered' })
                else:
                    Custom_user(first_name=name, username=username,password=password, email=email).save()
                    return render(request, 'add_user.html', {'form': form,'taken': 'Signup Success'})

            else:
                return render(request, 'add_user.html', {'form': form,'taken': 'Passwords do not match'})
    else:
        form = Signup_Form()
    return render(request, 'add_user.html', {'form': form})

@never_cache
def user_home(request):
    if 'username' in request.session:
        username = request.session['username']
        user = Custom_user.objects.get(username=username)

        if not user.is_superuser:
            return render(request, 'userHome.html')
        else:
            return redirect('adminHome')
    return redirect('loginpage')

@never_cache
def admin_login(request):
    if 'username' in request.session:
        username = request.session['username']
        user = Custom_user.objects.get(username=username)

        if user.is_superuser:
            return redirect('adminHome')
        else:
            return redirect('userHome')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Custom_user.objects.get(username=username, password=password)

            if user is not None:
                if user.is_superuser:
                    request.session['username'] = username
                    return redirect('adminHome')
                else:
                    return render(request, 'loginpage.html', {'user404': 'Please use user login'})

        except Custom_user.DoesNotExist:
            return render(request, 'loginpage.html', {'user404': 'Invalid Password or Username'})
    return render(request, 'adminlogin.html')

@never_cache
def admin_home(request):
    if 'username' in request.session:
        username = request.session['username']
        user = Custom_user.objects.get(username = username)

        if user.is_superuser:
            search = request.POST.get('search')

            if search:
                userDatas = Custom_user.objects.filter(username__istartswith = search)
            else:
                userDatas = Custom_user.objects.filter(is_superuser = False)
            return render(request, 'admin_Home.html', {'datas': userDatas})
    return redirect('loginpage')

def delete_user(request,id):
    user = Custom_user.objects.get(id = id)
    user.delete()
    return redirect('adminHome')

def edit_user(request,id):
    user =Custom_user.objects.get(id = id)
    return render(request, 'edit_user.html', {'user': user})

def update_data(request,id):
    user =Custom_user.objects.get(id = id)

    if request.method == 'POST':
        user.first_name = request.POST.get('name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()

        return redirect('adminHome')

    return redirect(request, 'editUser', {'user': user})



@never_cache
def logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect('loginpage')



