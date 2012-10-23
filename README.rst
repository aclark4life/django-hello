Hello Django
============

This is what **Hello World** in Django looks like to me.

settings.py::

    from hello import urls


    DEBUG = True
    ROOT_URLCONF = urls

urls.py::

    from django.conf.urls import patterns

    urlpatterns = patterns(
        '',
        (r'', 'hello.views.index'),
    )
    from django.http import HttpResponse
    import datetime


views.py::

    # Based on https://docs.djangoproject.com/en/1.4/topics/http/views/
    def index(request):
        """
        This function takes a Django request object and returns a 'Hello World'
        style response, by wrapping some HTML in a Django response object.
        """

        now = datetime.datetime.now()
        html = "<html><body>It is now %s.</body></html>" % now
        return HttpResponse(html)

Installation
------------

To install::

    $ git clone this-repo
    $ cd this-repo
    $ virtualenv .
    $ bin/pip install -r requirements.txt
    $ bin/django-admin.py runserver --settings=hello.settings

