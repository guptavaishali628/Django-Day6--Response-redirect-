from django.shortcuts import render, redirect
from django.urls import reverse  # import reverse function
from urllib.parse import urlencode

# Create your views here.
# method 1:
def redirect_page(req):
    # return redirect("https://www.google.com/")
    return redirect('home1')

def home1(req):
    return render(req,'home1.html')
    
# method 2(use reverse function):   
def redirect2(req):
    base_url = reverse('home2')
    return redirect(base_url)

def home2(req):
    return render(req,'home2.html')

# method 3(sending to url with specific data):
def redirect3(req):
    base_url = reverse('home3')
    data = urlencode({'name':'vaishali'})
    url=f'{base_url}?{data}'
    return redirect(url)

def home3(req):
    print(req.GET)
    return render(req,'home3.html')


    
