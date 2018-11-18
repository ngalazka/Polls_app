from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from polls.models import Question

def index(request):
    questions = Question.objects.all()
    questions = [(question.id, question.pub_date, question.question_text) for question in questions]
    return HttpResponse(questions)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)