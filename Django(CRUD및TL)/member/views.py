from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from member.models import *
# Create your views here.
class Member_List_View(ListView):
    model = Memberlist
    template_name = "member/member_list.html"
    context_object_name = 'members'


class Member_Create_View(CreateView):
    model = Memberlist
    fields = ['id','pw','tel','addr']
    template_name_suffix = "_create"
    success_url = reverse_lazy('m_list')

class member_update_view(UpdateView):
    model = Memberlist
    fields = ['id','pw','tel','addr']
    template_name_suffix = "_update"
    success_url = reverse_lazy('m_list')

class member_delete_view(DeleteView):
    model = Memberlist
    success_url = reverse_lazy('m_list')

class member_detail_view(DetailView):
    model = Memberlist
    fields = ['id', 'pw', 'tel', 'addr']
    template_name_suffix = "_detail"

