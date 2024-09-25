from django.shortcuts import render
from .models import Posts

# Create your views here.
def index(request):
    
    postss = Posts.objects.all()
    return render(request, 'index.html', {'posts': postss})

def post(request, pk):

    postss = Posts.objects.get(id=pk)
    return render(request, 'post.html', {'posts': postss})