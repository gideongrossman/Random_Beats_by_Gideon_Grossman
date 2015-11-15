from django.contrib import admin
from models import Question


# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Here\'s that Date information, dude', {'fields': ['pub_date']}),
    ]

	
admin.site.register(Question, QuestionAdmin)
