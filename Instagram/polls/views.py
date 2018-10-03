from django.shortcuts import render
from django.http import HttpResponse
from polls.models import User
from django.views.generic.edit import CreateView



def index(request):
    return HttpResponse("Instagram por Ana lucia ")

class PublicationView(CreateView):
    model = User
    fields = ['text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(User, self).form_valid(form)

# Create your views here.
