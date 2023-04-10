from django.shortcuts import render
from .forms import StudentRegistration

def showformdata(request):
    fm = StudentRegistration()
    return render(request,'enroll/userregistration.html', {'form':fm})

# from enroll.models import Student
# # Create your views here.
# def Studentinfo(request):
#     stud=Student.objects.all()
#     return render(request,'enroll/studetails.html',{'stu':stud})