from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)

        if user is None:
            context = {"error": "invalid username or password"}
            return render(request, "accounts/login.html", context=context)
        login(request, user)
        return redirect("/admin")
    return render(request, "accounts/login.html", {})