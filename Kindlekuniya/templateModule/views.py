from django.shortcuts import render

# Create your views here.
def index(req):
    title = 'Contact'
    context = {'title':title,}
    template = 'index.html'
    return render(req, template, context)