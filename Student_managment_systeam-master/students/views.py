from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import StudentsModel
from .forms import StudentForm

# Create your views here.
def index(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'student added succesfully')


            form=StudentForm()

    else:
        form=StudentForm()



    return render(request,'index.html',{'fm':form})

def Display(request):
    data=StudentsModel.objects.all()
    return render(request,'view_student.html',{'data':data})

def Delete_student(request,id):
    if request.method=='POST':
     stu=StudentsModel.objects.get(pk=id)
     stu.delete()


     return HttpResponseRedirect('/display')
def Edit_student(request,id):
  if request.method=='POST':
     stu = StudentsModel.objects.get(pk=id)
     form=StudentForm(request.POST,instance=stu)
     if form.is_valid():
         form.save()
         messages.success(request, 'student updated succesfully')

  else:
        stu = StudentsModel.objects.get(pk=id)
        form = StudentForm(request.POST, instance=stu)
  return render(request, 'update.html', {'form': form})
