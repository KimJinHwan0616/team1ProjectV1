from django.shortcuts import render
from django.views import View
# Create your views here.


# Player -> 선수1 감독 뷰
class CoachView(View):
    def get(self, request):
        return render(request, 'players/coach1.html')

    def post(self, request):
        pass


# Player -> 기록/순위 뷰
class RecordView(View):
    def get(self, request):
        return render(request, 'players/record.html')

    def post(self, request):
        pass