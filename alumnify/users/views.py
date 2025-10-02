from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from datetime import datetime



# Home page
def home_view(request):
    username = request.session.get('username', None)
    return render(request, "main/home.html", {'username': username})

# Signup
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        if password1 != password2:
            messages.error(request, "Passwords do not match")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            user = User.objects.create(
                user_id=f"user_{int(datetime.now().timestamp())}",
                username=username,
                email=email,
                password=password1,  # ⚠️ for real apps, hash passwords
                first_name=first_name,
                last_name=last_name,
                created_at=str(datetime.now())
            )
            messages.success(request, "Account created successfully! Please login.")
            return redirect("login")

    return render(request, "auth/signup.html")


# Login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username, password=password)

            # ✅ Save info in session
            request.session['user_id'] = user.user_id
            request.session['username'] = user.username

            # ✅ Set avatar in session
            if user.profile_pic:
                request.session['profile_pic'] = user.profile_pic.url
            else:
                request.session['profile_pic'] = None

            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("home")

        except User.DoesNotExist:
            messages.error(request, "Invalid username or password")

    return render(request, "auth/login.html")


# Logout
def logout_view(request):
    request.session.flush()  # Clear session
    messages.success(request, "Logged out successfully")
    return redirect("login")




def profile_view(request):
    user_id = request.session.get('user_id', None)
    if not user_id:
        messages.error(request, "You must be logged in to view your profile.")
        return redirect("login")

    user = User.objects.get(user_id=user_id)

    if request.method == "POST":
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")
        user.phone = request.POST.get("phone")
        user.bio = request.POST.get("bio")

        # Handle profile picture
        if request.FILES.get("profile_pic"):
            user.profile_pic = request.FILES["profile_pic"]

        user.save()

        # Update session avatar
        if user.profile_pic:
            request.session['profile_pic'] = user.profile_pic.url
        else:
            request.session['profile_pic'] = None

        messages.success(request, "Profile updated successfully!")
        return redirect("profile")

    return render(request, "main/profile.html", {"user": user})
