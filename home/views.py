from django.shortcuts import render
from django.views import View

# Create your views here.

# 메인화면 뷰
class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        pass

# 로그인 뷰
class LoginView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass

# 로그인 실패 뷰
class LoginfailView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass

# 로그아웃 뷰
class LogoutView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass

# 사이트맵 뷰
class SitemapView(View):
    def get(self, request):
        return render(request, 'sitemap.html')

    def post(self, request):
        pass