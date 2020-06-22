from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import DetailView, UpdateView, CreateView

from insta.models import Photo


def test(request):
    return HttpResponse("i am test!!!")


def selectAll(request):
    list = Photo.objects.all()
    return render(request, "insta/list.html", {"list": list})

class SelectOne(DetailView):
    model = Photo
    template_name = "insta/selectOne.html"

class PhotoUpload(CreateView):
    model = Photo
    fields = ["photo", "text"]
    template_name = "insta/upload.html"

    def form_valid(self, form):  # form에 있는걸 입력값으로 가져옴
        form.instance.author_id = self.request.user.id  # author_id 칼럼에서 1 일 때?

        if form.is_valid():  # from의 값이 유효하면
            form.instance.save()  # form에 있는 입력값을 저장
            return redirect("/insta/selectAll")  # 성공하면 rediect("/") 위치로 이동
        else:
            return self.render_to_response({"form": form})  # 실패하면 form데이터를 반환