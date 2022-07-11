from django.shortcuts import render
from django.views import View
# Create your views here.


# 이용약관 동의 뷰
class AgreeView(View):
    def get(self, request):
        # return render(request, 'join/agree.html')
        pass

    def post(self, request):
        pass

# 본인확인 뷰
class CheckmeView(View):
    def get(self, request):
        # return render(request, 'join/checkme.html')
        pass

    def post(self, request):
        pass


# 정보기입 뷰
class JoinmeView(View):
    def get(self, request):
        # return render(request, 'join/joinme.html')
        pass

    def post(self, request):
        pass


# 가입완료 뷰
class JoinokView(View):
    def get(self, request):
        # return render(request, 'join/joinok.html')
        pass

    def post(self, request):
        pass

# 회원가입관련 뷰
class ZipcodeView(View):
    pass

class UseridView(View):
    pass