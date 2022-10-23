from django.http import HttpResponse

# Create your views here.
def homePageView(request):
    return HttpResponse("hello, world - Bump Of Chicken")
    