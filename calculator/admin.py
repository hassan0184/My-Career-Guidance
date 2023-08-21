from django.contrib import admin
from .models import Subject,Level,SubjectGrade
class SubjectDisplay(admin.ModelAdmin):

    filter_horizontal = ('level',)


admin.site.register(Subject,SubjectDisplay)
admin.site.register(Level)
admin.site.register(SubjectGrade)
