from django.http import JsonResponse
from django.shortcuts import render

from chanleecrud.forms import StudentRegistration, CourseRegistration
from chanleecrud.models import User, Course


# Create your views here.
def home(request):
    form = StudentRegistration()
    students = User.objects.all()
    context = {'form': form, 'students': students}
    return render(request, 'chanleecrud/home.html', context)


# @csrf_exempt
def save_data(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            student_id = request.POST.get('student_id')
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            # When Edit button is not clicked
            if (student_id == ''):
                # Create new student object
                user = User(name=name, email=email, password=password)
            # When Edit button is clicked
            else:
                # Update Existing student object
                user = User(id =student_id, name=name, email=email, password=password)
            user.save()
            # Retrieve all students objects
            students = User.objects.values()
            print('students: ', students)
            # Convert Student queryset into list
            student_data = list(students)
            return JsonResponse({'status': 'Save',
                'student_data': student_data})
        else:
            # return JsonResponse({'status': 'Fail'})
            return JsonResponse({'status':0})
def delete_data(request):
    if request.method == 'POST':
        id = request.POST.get('student_id')
        obj = User.objects.get(pk=id)
        obj.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status':0})
# Edit data
def edit_data(request):
    if request.method == 'POST':
        id = request.POST.get('student_id')
        student = User.objects.get(pk=id)
        student_data = {
            'id': student.id,
            'name': student.name,
            'email': student.email,
            'password': student.password
        }
        return JsonResponse(student_data)

def course(request):
    form = CourseRegistration()
    courses = Course.objects.all()
    context = {'form': form, 'courses': courses}
    return render(request, 'chanleecrud/course.html', context)

def course_save_data(request):
    if request.method == 'POST':
        form = CourseRegistration(request.POST)
        if form.is_valid():
            course_id = request.POST.get('course_id')
            name = request.POST['name']
            description = request.POST['description']
            # When Edit button is not clicked
            if (course_id == ''):
                # Create new course object
                course = Course(name=name, description=description)
            # When Edit button is clicked
            else:
                # Update Existing course object
                course = Course(id=course_id, name=name, description=description)
            course.save()
            # Retrieve all courses objects
            courses = Course.objects.values()
            print('courses: ', courses)
            # Convert Course queryset into list
            course_data = list(courses)
            return JsonResponse({'status': 'Save',
                'course_data': course_data})
        else:
            # return JsonResponse({'status': 'Fail'})
            return JsonResponse({'status':0})

def course_delete_data(request):
    if request.method == 'POST':
        id = request.POST.get('course_id')
        obj = Course.objects.get(pk=id)
        obj.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status':0})
# Edit data
def course_edit_data(request):
    if request.method == 'POST':
        id = request.POST.get('course_id')
        course = Course.objects.get(pk=id)
        course_data = {
            'id': course.id,
            'name': course.name,
            'description': course.description,
        }
        return JsonResponse(course_data)
