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
    list_display = (..., 'audio_file_player', ...)
    actions = ['custom_delete_selected']

    def custom_delete_selected(self, request, queryset):
        #custom delete code
        n = queryset.count()
        for i in queryset:
            if i.audio_file:
                if os.path.exists(i.audio_file.path):
                    os.remove(i.audio_file.path)
            i.delete()
        self.message_user(request, ("Successfully deleted %d audio files.") % n)
    custom_delete_selected.short_description = "Delete selected items"
    
    def get_actions(self, request):
        actions = super(AudioFileAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
        fieldsets = [
        ('Beat Name', {'fields': ['beat_name', 'bass_kicks', 'snare_hits'], })
        ]	
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Beat, BeatAdmin)