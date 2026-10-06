from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse

#=====Decorator API VIEW
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BasicAuthentication
#========End DRF


from .forms import RegisterForm
# Create your views here.


class LoginView(ViewSet):
    permission_classes = [AllowAny]
    def login_fun(self, request):

        if request.user.is_authenticated:
            return redirect("users-dashboard")
        
        if request.method != 'POST':
            return render( request, "users/login.html")

        
        username = request.data.get("username", "").strip()
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is None:
           messages.error(request, "Invalid username or password.")
           return redirect("users-login")

        # Create authenticated session
        login(request, user)
        return redirect("users-dashboard")  
      

class RegisterView(ViewSet):
    permission_classes = [AllowAny]
    def register_fun(self, request):
        if request.user.is_authenticated:
            return redirect("users-dashboard")

        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect("users-dashboard")

        else:
            form = RegisterForm()

        return render(request, "users/register.html",{"form": form})


class DashboardView(ViewSet):
    def dashboard_fun(self, request):
        if not request.user.is_authenticated:
            return redirect("users-login")
        
        return render( request, "users/dashboard.html")
          
class LogoutView(ViewSet):
    def logout_fun(self, request):
        # Destroy the current authenticated session
        logout(request)
        #messages.success(request, "You have been logged out successfully.")
        return redirect("users-login")         