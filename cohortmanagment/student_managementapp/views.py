from django.shortcuts import render, redirect
from .models import Student, Cohort, Role, Status

# Create your views here.
def student_register(request):
    # this help form submission
    if request.method == 'POST':
        first_name = request.POST.get['first_name']
        last_name = request.POST.get['last_name']
        email = request.POST.get['email']
        role = Role.objects.get(id=request.POST['role'])
        status = Status.objects.get(id=request.POST['status'])
        cohort = Cohort.objects.get(id=request.POST['cohort'])
        
        
        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            role=role,
            status=status,
            cohort=cohort
        )
        return redirect('student.list')# redirect to student listing page after creation of student object
    
    roles = Role.objects.all()
    statuses = Status.objects.all()
    cohorts = Cohort.objects.all()
    
    return render(request, 'student_managementapp/student_register.html', {'roles': roles, 'statuses': statuses, 'cohorts': cohorts})

def students_search(request):
    students = Student.objects.all()  
    
# Addinig a filter logic for students
    role_id = request.GET.get('role')
    status_id = request.GET.get('cohort')
    cohort_id = request.GET.get('cohort')
    
    if role_id:
        student = students.filter(role_id=role_id)
    if status_id:
        student = students.filter(status_id=status_id)
    if cohort_id:
        student = students.filter(cohort_id=cohort_id)

    return render(request,'student_managementapp/student_list.html', {'students': students})
    