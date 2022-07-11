from django.shortcuts import render
from django.views import View
from teams.models import Stadiums

# Create your views here.


class TeamsView(View):
    def get(self, request):
        form = Stadiums.objects.get(hteam = '강원 FC')

        context = { 'stname': form.stname,
                    'opdate': form.opdate,
                    'hteam': form.hteam,
                    'accnum': form.accnum,
                    'addr': form.location,
                    'addrstmp': form.addrstmp,
                    'addrkey': form.addrkey
                    }

        return render(request, 'stadium_test.html', context)