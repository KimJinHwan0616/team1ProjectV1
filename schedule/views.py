from django.shortcuts import render
from django.views import View
# Create your views here.

# K리그 일정 -> K리그 1 뷰
class KL1View(View):
    def get(self, request):
        return render(request, 'schedule/kl1.html')

    def post(self, request):
        pass


# K리그 일정 -> K리그 2(준비 중) 뷰
class KL2View(View):
    def get(self, request):
        return render(request, 'schedule/kl2.html')

    def post(self, request):
        pass