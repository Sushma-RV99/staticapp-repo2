from django.shortcuts import render

# Create your views here.

def view1(request):
    myName="Sushma"
    favPlayer="Dhoni"
    favAnimal="Lion"
    favSubject="Python"
    d={'name':myName,'player':favPlayer,'animal': favAnimal,'subject':favSubject}
    return render(request,'staticApp1/1.html.txt',d)