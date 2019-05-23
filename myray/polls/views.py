from django.http import HttpResponse
def index(request):
    return HttpResponse("hello,world.you are at polls index")

# Create your views here.
