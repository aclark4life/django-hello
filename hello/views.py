from django.http import HttpResponse
import datetime


# Based on https://docs.djangoproject.com/en/1.4/topics/http/views/
def index(request):
    """
    This function takes a Django request object and returns a 'Hello World'
    style response, by wrapping some HTML in a Django response object.
    """

    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
