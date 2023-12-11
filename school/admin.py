from django.contrib import admin

from .models import Student, Teacher


# class StudentInline(admin.TabularInline):
#     model =

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']



