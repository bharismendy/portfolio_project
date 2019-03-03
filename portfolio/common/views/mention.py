from django.shortcuts import render


def mentions(request):
    return render(request, 'common/mentions.html')
