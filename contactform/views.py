from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView
# Create your views here.

def form(request):

    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        rollno = request.POST.get('rollno')
        mail = request.POST.get('mail')
        skill = request.POST.get('skill')

        contact.name = name
        contact.mail = mail
        contact.rollno = rollno
        contact.skill = skill
        contact.save()
        return HttpResponse("Thanks For Reaching Out !!")


    return render (request, 'form.html')


class HomePage(ListView):

    model = Post

    template_name = 'board.html'
    context_object_name = 'all_posts_list'



