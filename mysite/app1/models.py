from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=2000)
    def __str__(self):
        return self.question_text

@python_2_unicode_compatible
class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=5000)
    def __str__(self):
        return self.answer_text


