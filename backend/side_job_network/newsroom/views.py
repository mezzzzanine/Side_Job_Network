from django.shortcuts import render
from newsroom.models import News
from django.views.generic import DetailView
from django.core.paginator import Paginator

def newsroom(request):
    news = News.objects.all()

    # Set up paginators
    paginator = Paginator(News.objects.all(), 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "newsroom/newsroom.html", {'page_obj':page_obj, 'news':news})

class NewsDetailView(DetailView):
    model = News
    template_name = 'newsroom/news.html'
    context_object_name = 'news'

