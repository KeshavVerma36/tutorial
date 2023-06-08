from django.http import HttpResponse
import random
from django.template.loader import render_to_string
from tut.models import Articles




def home_view(request, *args, **kwargs): 
    number = random.randint(1,4)
    article_obj = Articles.objects.get(id=number)
    article_queryset = Articles.objects.all()

   
    context = {
        "object_list": article_queryset, 
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }
    

    html_string = render_to_string("home.html",context=context)

    return HttpResponse(html_string)