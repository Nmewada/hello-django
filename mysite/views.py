#I have created this file-Nitin
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # return HttpResponse("<center>This is Home Page..<br><a href='about'>About</a> <a href='services'>Services</a>  <a href='contact'>Contact</a></center>")
    # return render(request,'index.html')
    data={'name':'Nitin','place':'Mumbai'}
    return render(request,'index.html',data)

def about(request):
    return HttpResponse("This is About us Page..<a href='/'>Back</a>")

def services(request):
    return HttpResponse("This is Services Page..<a href='/'>Back</a>")

def contact(request):
    return HttpResponse("This is Contact us Page..<a href='/'>Back</a>")