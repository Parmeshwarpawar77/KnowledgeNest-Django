from django.shortcuts import render, get_object_or_404,redirect,HttpResponse
from .models import Student,BranchManager,Professor,Video,Course
from .forms import StudentForm,ProfessorForm,StudentLoginForm,VideoForm,CourseForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views.generic import ListView,CreateView,DetailView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect


#Student Profile For student

def student_profile(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    assigned_manager = BranchManager.objects.filter(branch_location=student.branch_location).first()

    context = {
        'student': student,
        'assigned_manager': assigned_manager,
    }

    return render(request, 'student_profile.html', context)

#Update Student Profile For student

def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            # Redirect to the student profile page after updating
            return redirect('student_profile', student_id=student_id)
    else:
        form = StudentForm(instance=student)

    return render(request, 'update_student.html', {'form': form})


# admin portal 

def admin_portal(request):
    return render(request, 'admin_portal.html')

#admin Portal - Student List

def student_list(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'student_list.html', context)

#Admin Portal - Professor list

def professor_list(request):
    professors = Professor.objects.all()
    context = {'professors': professors}
    return render(request, 'professor_list.html', context)

#admin portal - student details

def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    assigned_manager = BranchManager.objects.filter(branch_location=student.branch_location).first()

    context = {
        'student': student,
        'assigned_manager': assigned_manager,
    }
    return render(request, 'student_detail.html', context)

#Admin Portal Add Student

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

#Admin Portal Update Student

def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form, 'student': student})

#Admin Portal Update Student

def remove_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'remove_student.html', {'student': student})

#Admin Portal Update Professor

def add_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('professor_list')
    else:
        form = ProfessorForm()
    return render(request, 'add_professor.html', {'form': form})

#Admin Portal Update Professor

def update_professor(request, professor_id):
    professor = get_object_or_404(Professor, pk=professor_id)

    if request.method == 'POST':
        form = ProfessorForm(request.POST, request.FILES, instance=professor)
        if form.is_valid():
            form.save()
            return redirect('professor_list')
    else:
        form = ProfessorForm(instance=professor)

    return render(request, 'update_professor.html', {'form': form, 'professor': professor})

#Admin Portal Update Professor

def remove_professor(request, professor_id):
    professor = get_object_or_404(Professor, pk=professor_id)  

    if request.method == 'POST':
        professor.delete()
        return redirect('professor_list')
    return render(request, 'remove_professor.html', {'professor': professor})




#student 

def student_signup(request):
    form = StudentLoginForm()
    if request.method=='POST':
       form = StudentLoginForm(request.POST, request.FILES)
       if form.is_valid():
           user, user_profile = form.save()
           messages.success(request,"user Created Successfully")
           return redirect('slogin')
       else:
           messages.error(request,"""Your password can’t be too similar to your other personal information.
           Your password must contain at least 8 characters.
           Your password can’t be a commonly used password.
           Your password can’t be entirely numeric.""")
           
           form = StudentLoginForm()
    return render(request,"s_signup.html",{'form':form})

@csrf_protect
def student_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if username == 'admin' and password == 'skills':
            return redirect('admin_portal')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            user_profile = Student.objects.get(user=request.user)
            if user_profile.course_enrolled == 'Full stack':
                return render(request, 'dashboard_FSD.html',{'user_profile':user_profile})
            else:
                return render(request, 'dashboard_DS.html',{'user_profile':user_profile})  
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('slogin')
    return render(request,"s_login.html")

def student_logout(request):
        logout(request)
        messages.success(request,("you have loged out successfully"))
        return redirect("/")
    
#dashboard

def index(request):
    return render(request, 'index.html')

def fsd(request):
    return render(request,"FSD.html")

def ds(request):
    return render(request,"ds.html")



def dashboard(request):
    user_profile = Student.objects.get(user=request.user)
    if user_profile.course_enrolled == 'Full stack':
        return render(request, 'dashboard_FSD.html',{'user_profile':user_profile})


def dash(request):
    user_profile = Student.objects.get(user=request.user)
    if user_profile.course_enrolled == 'Data Science':
        return render(request, 'dashboard_DS.html',{'user_profile':user_profile})

def profile(request):
    return render(request,'dashboard/student_profile.html')

    
#video uploading

class djangoVideoListView(ListView):
    model = Video
    template_name = 'django_video_list.html'
    context_object_name = 'videos'
    
class djangoVideoCreateView(CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'django_video_form.html'
    success_url = 'courses/Django/videos/'
    
    def form_valid(self, form):
        form.instance.name  = self.kwargs['Django']
        return super().form_valid(form)
    

class pythonVideoListView(ListView):
    model = Video
    template_name = 'python_video_list.html'
    context_object_name = 'videos'
    
class pythonVideoCreateView(CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'python_video_form.html'
    success_url = 'courses/Python/videos/'
    
    def form_valid(self, form):
        form.instance.name  = self.kwargs['Python']
        return super().form_valid(form)
class webVideoListView(ListView):
    model = Video
    template_name = 'web_video_list.html'
    context_object_name = 'videos'
        
class webVideoCreateView(CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'web_video_form.html'
    success_url = 'courses/WEB/videos/'
    def form_valid(self, form):
        form.instance.name  = self.kwargs['WEB']
        return super().form_valid(form)
    
class sqlVideoListView(ListView):
    model = Video
    template_name = 'sql_video_list.html'
    context_object_name = 'videos'
    
class sqlVideoCreateView(CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'sql_video_form.html'
    success_url = 'courses/MySQL/videos/'
    def form_valid(self, form):
        form.instance.name  = self.kwargs['MySQL']
        return super().form_valid(form)
    
    
    
def COURSE(request):
    courses = Course.objects.all()
    return render(request,'course_list.html', {'courses': courses})
# def remove_course(request, course_id):
#     courses = get_object_or_404(Course, id=course_id)
#     if request.method == 'POST':
#         courses.delete()
#         return redirect('course_list')
#     return render(request, 'remove_course.html', {'courses': courses})

# def add_course(request):
#     if request.method == 'POST':
#         form = CourseForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('course_list')
#     else:
#         form = CourseForm()
#     return render(request, 'add_course.html', {'form': form})