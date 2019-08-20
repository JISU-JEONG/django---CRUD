from django.shortcuts import render, redirect
from .models import Article 

# Create your views here.
def index(request):
    articles = Article.objects.all()
    
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    article = Article.objects.create(title=title, context=content)
    context = {
        'id' : article.id
    }
    # return render(request, 'articles/creat.html', context)
    return redirect(f'/articles/{article.pk}/')

def detail(request, article_pk):
    article = Article.objects.get(pk = article_pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html',context)
