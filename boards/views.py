from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import NewTopicForm
from django.contrib.auth.decorators import login_required

from .models import (Board, Topic, Post)
# Create your views here.

def contact(request):
    return render(request, 'contact.html')
    
def index(request):
    obj = Post.objects.all()[:12]
    return render(request, 'index.html', {'obj': obj})

def listing(request):
    obj = Topic.objects.all()[:12]
    for i in obj:
        if i.image:
            print(i.image.url)
        else:
            print('no image')
    return render(request, 'listing.html', {'obj': obj})

def listing_details(request, pk):
    obj = Topic.objects.get(id = pk)
    return render(request, 'listing_details.html', {'obj': obj})

def home(request):
    boards = Board.objects.all()

    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    obj = board
    for i in obj.topics.all():
        if i.image:
            print(i.image.url)
        else:
            print('no image')
    return render(request, 'topics.html', {'board': board})

@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})


