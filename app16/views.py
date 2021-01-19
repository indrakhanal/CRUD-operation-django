from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .models import News
from .models import NewsComments


def index(request):
    #news1 = News(news_title='Title1', news_content='News Contents of News2')
    #news1.save()
    #news2 = News(news_title='Title2', news_content='News Contents of News2')
    #news2.save()
    news3 = News.objects.filter(pk=1)
    news3
    return HttpResponse(News.objects.all())


def sucess(request):
    return  render(request, 'app16/success_message.html')


class NewsView(ListView):
    context_object_name = 'all_news'
    queryset = News.objects.all()
    template_name='app16/news_list.html'


class NewsDetails(DetailView):
    model = News
    template_name = 'app16/news_details.html'


class NewsCreate(CreateView):
    template_name = 'app16/news_form.html'
    model = News
    fields = ['news_title','news_content']
    success_url = 'news'


class NewsUpdate(UpdateView):
    template_name = 'app16/news_form.html'
    model = News
    fields = ['news_title','news_content']
    success_url = 'news'


class NewsDelete(DeleteView):
    model = News
    success_url = 'news'