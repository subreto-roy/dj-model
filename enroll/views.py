from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print('Form Validated')
            print('Name:', fm.cleaned_data['name'])
            print('Email:', fm.cleaned_data['email'])
            # name = fm.cleaned_data['name']
            # email = fm.cleaned_data['email']
            # password = fm.cleaned_data['password']
            # print('Name:', name)
            #return render(request,'enroll/success.html', {'nm':name})
        else:
            fm = StudentRegistration()
        
    else:
        fm=StudentRegistration()
        
    return render(request, 'enroll/userregistration.html', {'form': fm})


# def showformdata(request):
#     fm = StudentRegistration()
#     return render(request,'enroll/userregistration.html', {'form':fm})

# from enroll.models import Student
# # Create your views here.
# def Studentinfo(request):
#     stud=Student.objects.all()
#     return render(request,'enroll/studetails.html',{'stu':stud})
