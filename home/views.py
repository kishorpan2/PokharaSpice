from .models import *
# from accounts.models import Profile
from django.contrib.auth.models import User
from django.contrib import messages 
from django.shortcuts import redirect, render
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
import bcrypt 
# Create your views here.
def home(request):
    return render(request,'home.html')


def login_attempt(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password = request.POST.get('password')
        user_obj= User.objects.filter(username= username).first 

        if user_obj is None:
            messages.success(request, 'User not found')
            return redirect('/login')
        user = authenticate(username= username, password=password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('/login')
        login(request, user)
        return redirect('/')
    return render(request, 'login.html')

def register_attempt(request):
    if request.method=='POST':
        username =request.POST.get('username')
        password =request.POST.get('password')
        hashed=bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        email =request.POST.get('email')
        try:
            if User.objects.filter(username=username).first():
                messages.success(request, 'Username is taken.')
                return redirect('/register')
            if User.objects.filter(email=email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/register')
            user_obj = User(username=username, email=email)
            user_obj.set_password(hashed)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user=user_obj, auth_token =auth_token)
            profile_obj.save()
            send_mail_after_registration(email, auth_token)
            return redirect('/token')

        except Exception as e:
            print(e) 
    return render(request , 'register.html') 

def success(request):
    return render(request, 'success.html')  

def token_send(request):
    return render(request , 'token_send.html')
    
def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )
        