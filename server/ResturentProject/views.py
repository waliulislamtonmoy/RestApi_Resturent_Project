from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Resturent Project Rest Api </h1>")
