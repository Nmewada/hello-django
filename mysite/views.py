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

def showdata(request):
    message=request.GET.get('message','default')
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    # return HttpResponse(message)
    purpose = ""
    strr = message
    if removepunc == "on":
        tempStr = ""
        purpose +=' | Removed Punctuations'
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in strr:
            if char not in punctuations:
                tempStr = tempStr + char
        params = {'purpose': 'Removed Punctuations', 'message_text': tempStr}
        strr = tempStr
    
    if fullcaps=="on":
        purpose +=' | Change To Uppercase'
        strr = strr.upper()
        params = {'purpose': 'Change To Uppercase', 'message_text': strr}

    if newlineremover=="on":
        tempStr = ""
        purpose +=' | Removed NewLines'
        for char in strr:
            if char!="\n":
                tempStr += char
        params = {'purpose': 'Removed NewLines', 'message_text': tempStr}
        strr = tempStr

    if extraspaceremover=="on":
        tempStr = ""
        purpose +=' | Removed Extra Space'
        for index, char in enumerate(strr):
            if not(strr[index] == " " and strr[index+1]==" "):
                tempStr += char
        params = {'purpose': 'Removed NewLines', 'message_text': tempStr}
        strr = tempStr



    params = {'purpose':purpose , 'message_text':strr}
    if(removepunc == "on" or fullcaps=="on" or newlineremover=="on" or extraspaceremover=="on"):
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Error')