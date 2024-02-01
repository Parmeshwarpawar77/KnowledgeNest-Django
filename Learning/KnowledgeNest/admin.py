from django.contrib import admin
from .models import Student, Professor, BranchManager,studentlog, Course, Video

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'course_enrolled', 'phone_number', 'email')
    
admin.site.register(Student, StudentAdmin)

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')    

admin.site.register(Professor, ProfessorAdmin)

class BranchManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

admin.site.register(BranchManager, BranchManagerAdmin)

class studentlogAdmin(admin.ModelAdmin):
    list_display=('username','password')

admin.site.register(studentlog,studentlogAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display=('title','course')
    search_fields= ['title']

admin.site.register(Course)
admin.site.register(Video,VideoAdmin)