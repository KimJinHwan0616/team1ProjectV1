from django.core.paginator import Paginator
from django.db.models import F
from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
from boards.models import Board, Comment        # Comment 모델 호출
from join.models import Member
from math import ceil

from urllib.parse import urlencode


class ListView(View):
    def get(self, request, perPage=25):
        form = request.GET.dict()
        qry = ''

        if request.GET.get('fkey') is not None and \
            request.GET.get('ftype') is not None:
            # 검색유형이 제목이라면
            if form['ftype'] == 'title':
                bdlist = Board.objects.select_related().\
                    filter(title__contains=form['fkey'])
            elif form['ftype'] == 'userid':
                bdlist = Board.objects.select_related().filter(member__userid=form['fkey'])
            elif form['ftype'] == 'contents':
                bdlist = Board.objects.select_related().filter(contents__contains=form['fkey'])
            # get으로 전송된 키와 값을 인코딩해서 질의문자열로 변환
            qry = urlencode({'ftype': form['ftype'], 'fkey': form['fkey']})
            # print(qry)
        else:
        # 검색어와 검색대상이 없는 경우
            bdlist = Board.objects.select_related()


        # 페이징 기타처리 #
        # 총 페이지수 = 전체게시물수 / 페이지당게시물수
        pages = ceil(bdlist.count() / perPage)

        # 페이징 처리1
        # 전체 Board 데이터를 페이지당 25개씩 나눠 페이지별로 저장
        # paginator = Paginator(bdlist, perPage)
        #
        # 질의문자열 중 cpage가 존재한다면
        # if request.GET.get('cpage') is not None:
        #     cpage를 이용해서 해당 페이지의 데이터를 가져옴
        #     bdlist = paginator.get_page(form['cpage'])
        # else:
        #     bdlist = paginator.get_page(1)

        # 페이징 처리2
        # select id, title, userid, regdate, views from board
        # limit ?, 25;
        # 1page : limit 0, 25   (시작위치, 가져올갯수)
        # 2page : limit 25, 25
        # 3page : limit 50, 25
        # Npage : limit 25*(N -1), 25
        cpage = 1
        if request.GET.get('cpage') is not None:
            cpage = form['cpage']
        start = (int(cpage)-1) * perPage
        end = start + perPage
        # bdlist에서 start에서 end까지의 데이터를 가져옴
        bdlist = bdlist[start:end]

        # cpage 1 : 1 2 3 4 5 6 7 8 9 10
        # cpage 7 : 1 2 3 4 5 6 7 8 9 10
        # cpage 10 : 1 2 3 4 5 6 7 8 9 10

        # cpage 11 : 11 12 13 14 15 16 17 18 19 20
        # cpage 15 : 11 12 13 14 15 16 17 18 19 20

        # cpage N : stpgn = int(N / 10) * 10 + 1

        stpgn = int( (int(cpage) - 1) / 10) * 10 + 1

        context = {'bds': bdlist, 'pages': pages, 'range': range(stpgn, stpgn + 10), 'qry': qry}
        return render(request, 'boards/list.html', context)

    def post(self, request):
        pass


class ViewView(View):
    def get(self, request):
        form = request.GET.dict()

        # 조회수 증가
        Board.objects.filter(id=form['bno'])\
            .update(views=F('views') + 1)

        # select * from board join member
        # on b.member = m.id where b.id = *
        bd = Board.objects.select_related().get(id=form['bno'])

        # select * from comment join board ~ join member ~      # SQL문
        # where board = ?
        # order by cno
        cmt = Comment.objects.select_related()\
            .filter(board__id=form['bno']).order_by('cno', 'id')       # ORM문

        # 로그인 아이디 추출
        lgnusr = ''
        if request.session.get('userinfo') is not None:
            lgnusr = request.session.userinfo.split('|')[0]

        context = {'bd': bd, 'cmt': cmt, 'lgnusr': lgnusr}                        # cmt, lgnusr 변수 설정 -> view.html
        return render(request, 'boards/view.html', context)


class WriteView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


class ModifyView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


class RemoveView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


# board 테이블 데이터 초기화 (1000개)
class SetupView(View):
    def get(self, request):
        pass
        # for i in range(350):
        #     # insert into board (title, member, contents)
        #     # values (*, *, *)
        #     b = Board(title='워크래프트 고블린',
        #               member=Member.objects.get(id=1),   # abc123
        #               contents='시간은 금이라구, 친구')
        #     b.save()
        #
        #     b = Board(title='스탠포드대 스티브잡스',
        #               member=Member.objects.get(id=3),   # 987xyz
        #               contents='스테이 헝그리, 스테이 풀리시')
        #     b.save()
        #
        #     b = Board(title='무명',
        #               member=Member.objects.get(id=4),  # 4i5j6k
        #               contents='만약, 당신이 실패했다면, 도전했다는 증거다')
        #     b.save()
        #
        # return redirect('/')


class CmntView(View):
    def post(self, request):
        form = request.POST.dict()

        # 댓글의 가장 최근 id값을 알아냄
        id = Comment.objects.latest('id').id

        c = Comment(cno=id+1,
                    board=Board.objects.get(id=form['bno']),
                    member=Member.objects.get(userid=form['userid']),
                    comments=form['comments'])
        c.save()

        return redirect('/board/view?bno=' + form['bno'])

