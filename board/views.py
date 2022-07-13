from django.db.models import F
from django.shortcuts import render
from math import ceil, floor
from urllib.parse import urlencode

# def board(request):
#     return render(request, 'board/news.html')
#
# def announce(request):
#     return render(request, 'board/announce.html')
#
# def team(request):
#     return render(request, 'board/team.html')
from django.views import View

from board.models import News

class NewsView(View):
    def get(self, request, perPage=8):
        form = request.GET.dict()
        query = ''

        if request.GET.get('keyword') is not None and request.GET.get('type') is not None:

            if form['type'] == 'title':
                news_table = News.objects.select_related().\
                    filter(title__contains=form['keyword'])
            elif form['type'] == 'content':
                news_table = News.objects.select_related().\
                    filter(content__contains=form['keyword'])

            query = urlencode({'type': form['type'], 'keyword': form['keyword']})

        else:
            news_table = News.objects.select_related()  #

        pages = ceil(news_table.count() / perPage )  # 전체 페이지 수

        page = 1
        if request.GET.get('page') is not None:
            page = form['page']

        start = (int(page) - 1) * perPage
        end = start + perPage

        news_table = news_table[start:end]
        listPage = int((int(page) - 1) / 10) * 10 + 1

        context = {'nt': news_table, 'pages': pages, 'range': range(listPage, listPage + 10), 'query': query }
        return render(request, 'board/news.html', context)

    def post(self, request):
        pass

class AnnounceView(View):
    def get(self, request, perPage = 8):
        form = request.GET.dict()
        query = ''

        if request.GET.get('keyword') is not None and request.GET.get('type') is not None:

            if form['type'] == 'title':
                announce_table = News.objects.select_related().\
                    filter(category__contains='notice', title__contains=form['keyword'])
            elif form['type'] == 'content':
                announce_table = News.objects.select_related().\
                    filter(category__contains='notice', content__contains=form['keyword'])

            query = urlencode({'type': form['type'], 'keyword': form['keyword']})

        else:
            announce_table = News.objects.select_related().filter(category__contains='notice')
            # announce_table = News.objects.select_related()

        pages = ceil ( announce_table.count() / perPage )

        page = 1
        if request.GET.get('page') is not None:
            page = form['page']

        start = ( int(page)-1 ) * perPage
        end = start + perPage

        announce_table = announce_table[start:end]
        listPage = int( (int(page) - 1) / 10) * 10 + 1

        context = {'at': announce_table, 'pages': pages, 'range': range(listPage, listPage + 10), 'query': query}

        return render(request, 'board/announce.html', context)

    def post(self, request):
        pass

class TeamplayerView(View):
    def get(self, request, perPage = 8):
        form = request.GET.dict()
        query = ''

        if request.GET.get('keyword') is not None and request.GET.get('type') is not None:

            if form['type'] == 'title':
                teamplayer_table = News.objects.select_related().\
                    filter(category__contains='club', title__contains=form['keyword'])
            elif form['type'] == 'content':
                teamplayer_table = News.objects.select_related().\
                    filter(category__contains='club', content__contains=form['keyword'])

            query = urlencode({'type': form['type'], 'keyword': form['keyword']})

        else:
            teamplayer_table = News.objects.select_related().filter(category__contains='club')

        pages = ceil( teamplayer_table.count() / perPage )        # 전체 페이지 수

        page = 1
        if request.GET.get('page') is not None:
            page = form['page']

        start = (int(page) - 1) * perPage
        end = start + perPage

        teamplayer_table = teamplayer_table[start:end]
        listPage = int((int(page) - 1) / 10) * 10 + 1

        context = {'tt': teamplayer_table, 'pages': pages, 'range': range(listPage, listPage + 10), 'query': query}

        return render(request, 'board/teamplayer.html', context)

    def post(self, request):
        pass

##

class News_detailView(View):
    def get(self, request):
        form = request.GET.dict()

        News.objects.filter(id=form['no']).update( view = F('view') + 1 )      # 조회수 증가

        news_table = News.objects.select_related().get(id=form['no'])        #

        nextone = News.objects.filter(id__gt=form['no'])[0].id

        prevno = News.objects.filter(id__lt=form['no'])[0].id
        nextno = News.objects.filter(id__gt=form['no']).order_by('id')[0].id

        print(f'이전: {prevno}, 다음: {nextno}, 마지막: {nextone}')

        context = {'nt': news_table, 'prevno': prevno, 'nextno': nextno, 'nextone': nextone}
        return render(request, 'board/news_detail.html', context)

class Announce_detailView(View):
    def get(self, request):
        form = request.GET.dict()

        News.objects.filter(id=form['no'], category__contains='notice').update(view=F('view') + 1)      # 조회수 증가

        announce_table = News.objects.select_related().filter(category__contains='notice').get(id=form['no'])

        nextone = News.objects.filter(category__contains='notice', id__gte=form['no'])[0]


        context = {'at': announce_table, 'nextone': nextone}

        return render(request, 'board/announce_detail.html', context)

    def post(self, request):
        pass

class Teamplayer_detailView(View):
    def get(self, request):
        form = request.GET.dict()

        News.objects.filter(id=form['no'], category__contains='club').update(view=F('view') + 1)      # 조회수 증가

        teamplayer_table = News.objects.select_related().filter(category__contains='club').get(id=form['no'])

        num1 = News.objects.select_related().filter(category__contains='club').order_by('-id')[0]      # 번호 역순 - 마지막번

        num2 = News.objects.select_related().filter(category__contains='club').order_by('id')[0]       # 번호 순 - 1번

        context = {'tt': teamplayer_table, 'num1': num1, 'num2': num2}

        return render(request, 'board/teamplayer_detail.html', context)

    def post(self, request):
        pass
