from django.shortcuts import render

from .models import Talk


def talk_list(request):
    talks = Talk.objects.all()
    context = {'talks': talks}
    return render(request, 'talks/talk_list.html', context)
