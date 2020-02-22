from django.shortcuts import render,redirect
from .models import StudentData
# Create your views here.
def home(request):
    students=StudentData.objects.all()
    return render(request,'student/home.html',{'student':students})

def add_student_view(request):
    return render(request,'student/addstudent.html')


def save_student_data(request):
    roll=request.POST.get('roll')
    fname=request.POST.get('fname')
    lname=request.POST.get('lname')
    sclass=request.POST.get('sclass')
    section=request.POST.get('section')
    telgu=request.POST.get('telgu')
    hindi=request.POST.get('hindi')
    eng=request.POST.get('eng')
    math=request.POST.get('math')
    science=request.POST.get('science')
    social=request.POST.get('social')


    data=StudentData(
        roll=roll,
        first_name=fname,
        last_name=lname,
        student_class=sclass,
        student_section=section,
        telgu_mark=telgu,
        hindi_mark=hindi,
        english_mark=eng,
        math_mark=math,
        science_mark=science,
        social_mark=social
    )
    data.save()

    return redirect('/')

def edit_view(request,id):
    student=StudentData.objects.get(pk=id)
    return render(request,'student/edit.html',{'student':student})

def update_view(request,id):
    student=StudentData.objects.get(pk=id)
    student.roll=request.POST.get('roll')
    student.first_name=request.POST.get('fname')
    student.last_name=request.POST.get('lname')
    student.student_class=request.POST.get('sclass')
    student.student_section=request.POST.get('section')
    student.telgu_mark=request.POST.get('telgu')
    student.hindi_mark=request.POST.get('hindi')
    student.english_mark=request.POST.get('eng')
    student.math_mark=request.POST.get('math')
    student.science_mark=request.POST.get('science')
    student.social_mark=request.POST.get('social')
    student.save()
    return redirect('/')

def delete_view(request, id):
        student = StudentData.objects.get(pk=id)
        student.delete()
        return redirect('/')
