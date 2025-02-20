from django.contrib import admin
from dashboard.models import Notes,Homework,Todo

class NotesAdmin(admin.ModelAdmin):
    list_display = ['user','title','description']
admin.site.register(Notes,NotesAdmin)

class HomeworkAdmin(admin.ModelAdmin):
    list_display = ['user','subject','title','description','due','is_finished']
admin.site.register(Homework,HomeworkAdmin)

class TodoAdmin(admin.ModelAdmin):
    list_display = ['user','title','is_finished']
admin.site.register(Todo,TodoAdmin)