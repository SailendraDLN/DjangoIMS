from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
# Create your views here.
def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = { "object": article_obj }
    return render(request, "articles/detail.html", context=context)

def article_search_view(request):
    #print(dir(request))
    query_dict = request.GET #this is a dictionary
    #query = query_dict.get("q") #<input type="text" name="q"  />
    try:
        query = int(query_dict.get("q"))
    except:
        query = None
    article_obj = None #setting a default value of none to article
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {
        "object": article_obj
    }
    return render(request,"articles/search.html",context=context)

@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = { "form" : form }
    if form.is_valid():
        article_obj = form.save()
        """
        to re-render the form and save the posted data in db,
        comment the context[object]and context[created] assignments 
        and re initialize the form as so: context['form'] = ArticleForm()
        """
        # title = form.cleaned_data.get('title')
        # content = form.cleaned_data.get('content')
        # article_obj = Article.objects.create(title=title, content=content)
        context['object'] = article_obj
        context['created'] = True
    # if request.method == "POST":
    #     title = request.POST.get("title")
    #     content = request.POST.get("content")
    #     article_obj = Article.objects.create(title=title,content=content)
    #     context["object"] = article_obj
    #     context["created"] = True
    return render(request, "articles/create.html", context=context)
