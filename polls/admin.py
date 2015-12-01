from django.contrib import admin
from models import Question, Choice, Beat


# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Here\'s that Date information, dude', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    
class BeatAdmin(admin.ModelAdmin):
    fieldsets = [
    ('Beat Name', {'fields': ['beat_name', 'bass_kicks', 'snare_hits'], })
    ]	
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Beat, BeatAdmin)