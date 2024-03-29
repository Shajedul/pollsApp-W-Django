from django.contrib import admin
from .models import Question, Choice
admin.site.site_header = "Poll App"
admin.site.site_title = "Poll Dashboard"
admin.site.index_title = "Welcome to Polls Central"
# admin.site.register(Question)
# admin.site.register(Choice)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAadmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAadmin)