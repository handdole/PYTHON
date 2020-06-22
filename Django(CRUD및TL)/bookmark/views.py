from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *

from bookmark.models import Bookmark


class BookDetail(DetailView):
    model = Bookmark

class BookDelete(DeleteView):
    model = Bookmark
    # template_name_suffix = '_delete'
    success_url = reverse_lazy('list')

class BookUpdate(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update'
    success_url = reverse_lazy('list')

class BookCreate(CreateView):
    model = Bookmark
    fields = ['site_name','url']
    #입력하는 template 필요
    template_name_suffix = '_create'


    #성공했으면 어느 페이지로 연결할지 설정
    #호출했던 위치에 상관없이 urls에서 name으로
    #명명된 페이지를 호출해 준다.
    success_url = reverse_lazy('list')

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 5
    template_name = "bookmark/bookmark_list.html"
    context_object_name = "posts"


def index(request , id , pw ):
    return HttpResponse('received id : ' + id +'<br>'+ 'received pw : '+ pw)