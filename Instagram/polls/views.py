from django.shortcuts import render
from django.http import HttpResponse
from polls.models import User
from polls.models import Post
from polls.models import Follow
from django.views.generic.edit import CreateView
from django.views.generic import ListView

def menu(request):
    return HttpResponse("Bienvenido a instagram! si quiere ver usuarios vaya a usuarios/ si quiere ver publicaciones vaya a post/")
def index(request):
    latest_question_list = User.objects.order_by('-created_at')[:5]
    output = ', '.join([u.text for u in latest_question_list])
    return HttpResponse(output)
def post(request):
    latest_question_list = Post.objects.order_by('-pub_date')[:5]
    output = ', '.join([u.headline for u in latest_question_list])
    return HttpResponse(output)
def follow(request):
    latest_question_list = Follow.objects.order_by('-created_at')[:5]
    output = ', '.join([u.target for u in latest_question_list])
    return HttpResponse(output)

def detail(request, user_id):
    return HttpResponse("Bienvenidos a Usuarios %s." % user_id)
def results(request, user_id):
    response = "los usuarios ingresados %s."
    return HttpResponse(response % user_id)
def vote(request, user_id):
    return HttpResponse("El usuario ingresado %s." % user_id)
# Create your views here.
