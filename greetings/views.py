from django.http import HttpResponse


# Create your views here.

def hello(request):
    """ Basic Starting Point for the applications.

    :param request:
    :return: Static String Hello World
    """
    return HttpResponse("Hello, world!")
