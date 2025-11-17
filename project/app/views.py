from django.shortcuts import render, redirect

# Create your views here.
def redirect_page(req):
    return redirect("https://www.google.com/")
