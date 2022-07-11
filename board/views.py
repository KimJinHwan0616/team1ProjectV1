from django.db.models import F
from django.shortcuts import render
from math import ceil
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
    def get(self, request, perPage=12):
        form = request.GET.dict()
        query = ''

        if request.GET.get('key') is not None and request.GET.get('type') is not None:

            if form['type'] == 'title':
                news_table = News.objects.select_related().\
                    filter(title__contains=form['key'])
            elif form['type'] == 'content':
                news_table = News.objects.select_related().\
                    filter(content__contains=form['key'])

            query = urlencode({'type': form['type'], 'key': form['key']})

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

        context = {'nt': news_table, 'pages': pages, 'range': range(listPage, listPage + 10) }
        return render(request, 'board/news.html', context)

    def post(self, request):
        pass

class AnnounceView(View):
    def get(self, request, perPage = 8):
        form = request.GET.dict()
        query = ''

        if request.GET.get('key') is not None and request.GET.get('type') is not None:

            if form['type'] == 'title':
                announce_table = Announce.objects.select_related().filter(title__contains=form['key'])
            elif form['type'] == 'content':
                announce_table = Announce.objects.select_related().filter(contents__contains=form['key'])

            query = urlencode({'type': form['type'], 'key': form['key']})

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


class DetailView(View):
    def get(self, request):
        form = request.GET.dict()

        News.objects.filter(id=form['no'], category__contains='notice').update(view=F('view') + 1)      # 조회수 증가

        announce_table = News.objects.select_related().filter(category__contains='notice').get(id=form['no'])

        context = {'announce_table': announce_table}

        return render(request, 'board/detail.html', context)

    def post(self, request):
        pass


class Detail2View(View):
    def get(self, request):
        form = request.GET.dict()

        News.objects.filter(id=form['no'], category__contains='club').update(view=F('view') + 1)      # 조회수 증가

        teamplayer_table = News.objects.select_related().filter(category__contains='club').get(id=form['no'])

        context = {'teamplayer_table': teamplayer_table}

        return render(request, 'board/detail2.html', context)

    def post(self, request):
        pass


class News_detailView(View):
    def get(self, request):
        form = request.GET.dict()

        News.objects.filter(id=form['no']).update( view = F('view') + 1 )      # 조회수 증가

        news_table = News.objects.select_related().get(id=form['no'])        #

        context = {'nt': news_table}
        return render(request, 'board/news_detail.html', context)