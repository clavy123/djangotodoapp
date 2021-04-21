from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todoapp
from .forms import TodoForm
def todo(request):
    data=request.POST.get('num1','default')
    x=Todoapp(text=data)
    x.save()
    item=Todoapp.objects.all()
    print(data)
    return render(request,'index.htm',{'items':item})
def update(request,pk):
    data=Todoapp.objects.get(id=pk)
    form=TodoForm(instance=data)
    if request.method=='POST':
        form=TodoForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("todo")
    context={'form':form}
    return render(request,'update.htm',context)
def delete(request,pk):
    y=Todoapp.objects.get(id=pk)
    y.delete()
    return redirect("todo")