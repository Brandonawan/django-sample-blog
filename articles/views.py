from django.shortcuts import render
from .models import Article

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request,'articles/article_list.html', {'articles': articles})

def homepage(request):
    #return HttpResponse("homepage")
    return render(request, 'articles/homepage.html')

def about(request):
    #return HttpResponse("about")
    return render(request, 'articles/about.html')