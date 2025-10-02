from django.shortcuts import render

def home_view(request):
    return render(request, "main/home.html")  # path must match templates/main/home.html
