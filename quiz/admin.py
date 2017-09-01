from django.contrib import admin

from .models import Answer, Exam, Subject, Question


admin.site.register(Answer)
admin.site.register(Exam)
admin.site.register(Subject)
admin.site.register(Question)
