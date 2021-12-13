from django.http import HttpResponse


def index_page(request):
    # create a HttpResponse object and return it.
    response = HttpResponse('Hello World', content_type="text/plain")
    return response