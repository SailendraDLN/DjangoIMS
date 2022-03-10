from django.http import HttpResponse
from articles.models import Article
from django.shortcuts import render
from django.template.loader import render_to_string



def home_view(request):
    article_obj = Article.objects.get(id=1)
    my_list = Article.objects.all()
    context = {
        "my_list":my_list,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }
    HTML_STRING = render_to_string("home_view.html", context=context)
    #return render(request, "home_view.html", context)
    return HttpResponse(HTML_STRING)