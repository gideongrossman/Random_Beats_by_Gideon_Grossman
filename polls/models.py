from django.db import models
import datetime
from django.utils import timezone

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
    class Meta:
        get_latest_by = 'creation_date'
    def __str__(self):
        return self.beat_name
    def save(self, force_insert=False, force_update=False, using=None):
        if self.beat_name == "Harry":
            self.beat_name = "Hairy Hairy Harry (Harry is Hairy!)"
        super(Beat, self).save() # Call the "real" save() method.