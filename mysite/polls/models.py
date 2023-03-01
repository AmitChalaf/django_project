from django.db import models
from django.utils import timezone
import datetime
from django.core import validators
import django.forms as forms


# Create your models here.
def validateCleanLang(value):
    CURSES = ('dumbass', 'moron')
    for curse in CURSES:
        if curse in value:
            raise forms.ValidationError('Bad word detected')
    return value



class Question(models.Model):
    question_text = models.CharField(max_length=200, validators=[validateCleanLang, validators.MinLengthValidator(5)])
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)# last 24 hours


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text