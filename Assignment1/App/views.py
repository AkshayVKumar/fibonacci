from django.shortcuts import render
from App.forms import Form_data
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.

def fibo(n):
    if n==1 or n==2:
        return 1
    return fibo(n-1)+fibo(n-2)
    
def index(request):
    if request.method=='POST':
        form=Form_data(request.POST)
        if form.is_valid():
            data=form.cleaned_data['Data']
            print(data)
            return HttpResponse("{}".format(fibo(data)))
    else:
        form=Form_data()
    form_data={'form_data':form}

    return render(request,"index.html",context=form_data)

def output(request):
    return HttpResponse("hello world")