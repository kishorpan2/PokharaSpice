from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
class RegisterView(APIView):
    def post(self,request):
        username=request.data['username']
        password=request.data['password']
        user = User(username=username)
        user.set_password(password)
        user.save()
        refresh = RefreshToken.for_user(user)

        return {
        'status':'success',
        'refresh': str(refresh),'user_id':user.id,
        'access': str(refresh.access_token),
    }
