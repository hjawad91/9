from django.shortcuts import render
from django.views import generic
from .models import Question,Answer
# Create your views here.

class IndexView(generic.ListView):
    template_name='app1/index.html'
    context_object_name= 'question_list'
    def get_queryset(self):
        return Question.objects.all
