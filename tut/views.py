from django.shortcuts import render
from .models import Articles
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm

# Create your views here.
def article_search_view(request):
    query_dict = request.GET

    try:
        query = int(query_dict.get("q"))
    except:
        query = None    
    article_obj= None
    if query is not None:
        article_obj = Articles.objects.get(id=query)
    context ={
        "object": article_obj
    }
    return render(request, "articles/search.html",context=context)


@login_required 
def article_create_view(request):
    #print(request.POST)
    form = ArticleForm(request.POST or None)
    context = {
        "form" : form   
    }

    if form.is_valid():
        article_object = form.save()
        context["object"] = article_object
        context["created"] = True       
    return render(request, "articles/create.html", context=context) 


 
def article_detail_view(request, id, *args, **kwargs):
    article_obj = None
    if id is not None:
        article_obj = Articles.objects.get(id=id)
    context = {
        "object": article_obj,
    }
    return render(request, "articles/details.html", context=context)