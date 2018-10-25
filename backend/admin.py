from django.contrib import admin

from .models import Question, QuestionLink

admin.site.register(Question)
admin.site.register(QuestionLink)
