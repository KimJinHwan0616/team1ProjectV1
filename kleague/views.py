from django.shortcuts import render
from django.views import View
# Create your views here.

# K리그 일정 -> K리그 1 뷰
class MapView(View):
    def get(self, request):
        return render(request, 'kleague/map.html')

    def post(self, request):
        pass
