from django.shortcuts import render


def index(request):
    title = 'главная'
    content = {"title": title}
    return render(request, 'mainapp/index.html', context=content)
