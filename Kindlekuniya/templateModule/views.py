from django.shortcuts import render

# Create your views here.
def index(req):
    title = 'Contact'
    context = {'title':title,}
    template = 'index.html'
    return render(req, template, context)

def genres(req):
    title = 'Contact'
    context = {'title':title,}
    template = 'genres.html'
    return render(req, template, context)