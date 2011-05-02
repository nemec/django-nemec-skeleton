from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse

def index(req):
  return HttpResponse("Welcome to the index page! Please add views as required "
                      "by your application.")

