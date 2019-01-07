from django.contrib import admin

from .models import Question, QuestionLink


class QuestionLinkInline(admin.TabularInline):
    model = QuestionLink
    fk_name = 'target'
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = (QuestionLinkInline,)


admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionLink)
