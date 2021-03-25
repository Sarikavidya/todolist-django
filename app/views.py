from django.shortcuts import render,redirect,HttpResponse
from .models import Task
from .forms import TaskForm,UpdateForm
# Create your views here.
def app(request):
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:app')

    tasks= Task.objects.all()
    form = TaskForm()
    print(form)
    return render(request,'index.html', {'tasks':tasks, 'form':form})

def edit(request, id=id):
    task = Task.objects.get(id=id)
    if request.method=='POST':
        form = UpdateForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            return redirect('app:app')


    form = UpdateForm(request.POST or None, instance=task)
    print(form)
    return render(request,'edit.html', {'form':form})

def completed(request, id):
    task = Task.objects.get(id=id)
    if task.completed != True:
        task.completed = True
        task.save()
        return redirect('app:app')

def delete(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('app:app')

def filter_priority(request,choice):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('app:app')
    tasks = Task.objects.filter(priority=choice)
    form = TaskForm()
    print(form)
    return render(request,'index.html', {'tasks':tasks,'form':form})


def filter_status(request,choice):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('app:app')
    tasks = Task.objects.filter(completed=choice)
    form = TaskForm()
    print(form)
    return render(request,'index.html', {'tasks':tasks,'form':form})
