from django.http import HttpResponse

def index(request):
    return HttpResponse("Hey Bingo, You're at the polls index")
