from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . models import Task
from django import forms
from django.views.generic import ListView, DeleteView
from django.views.generic import DetailView
from django.views.generic import UpdateView


class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task_key'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'taask'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'form'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

def add(request):
    task2=Task.objects.all()
    if request.method == 'POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task1=Task(name=name,priority=priority,date=date) #creating row in database table.
        task1.save()
    return render(request,'home.html',{'task_key':task2})

def delete(request,taskid):
    task3=Task.objects.get(id=taskid)
    if request.method == 'POST':
        task3.delete()
        #return redirect('/')    #return to homepage
    return render(request,'delete.html')

def update(request,id):
    task4=Task.objects.get(id=id)
    form1=TodoForm(request.POST or None,instance=task4)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request,'edit.html',{'form1_key':form1,'task4_key':task4})


class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields=['name','priority','date']
