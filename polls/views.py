from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from polls.models import Question

def index(request):
    questions = Question.objects.all()
    questions = [(question.id, question.pub_date, question.question_text) for question in questions]
    return HttpResponse(questions)
