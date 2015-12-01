from django.conf import settings
import os.path
from django.db import models
import datetime
from django.utils import timezone
from audiofield.fields import AudioField

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
        
class Beat(models.Model):
    beat_name = models.CharField(max_length=200)
    snare_hits = models.CharField(max_length=200, default = "empty")
    bass_kicks = models.CharField(max_length=200, default = "empty")
    creation_date = models.DateTimeField(auto_now_add = True, editable=False, null=True)
    audio_file = AudioField(upload_to='your/upload/dir', blank=True,
                        ext_whitelist=(".mp3", ".wav", ".ogg"),
                        help_text=("Allowed type - .mp3, .wav, .ogg"))
                        
    def audio_file_player(self):
    #audio player tag for admin
        if self.audio_file:
            file_url = settings.MEDIA_URL + str(self.audio_file)
            player_string = '<ul class="playlist"><li style="width:250px;">\
            <a href="%s">%s</a></li></ul>' % (file_url, os.path.basename(self.audio_file.name))
            return player_string
        
    audio_file_player.allow_tags = True
    audio_file_player.short_description = ('Audio file player')

    class Meta:
        get_latest_by = 'creation_date'
    def __str__(self):
        return self.beat_name