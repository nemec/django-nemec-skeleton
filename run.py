#!/usr/bin/python
from gevent import monkey; monkey.patch_all()
from gevent.wsgi import WSGIServer
import sys
import os
import traceback
from django.core.handlers.wsgi import WSGIHandler
from django.core.management import call_command
from django.core.signals import got_request_exception

PROJECT_NAME = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(os.path.abspath('..'))
os.environ['DJANGO_SETTINGS_MODULE'] = PROJECT_NAME + '.settings'

if len(sys.argv) > 1:
  os.environ['DJANGO_SETTINGS_MODULE'] += '.%s' % sys.argv[1]


def exception_printer(sender, **kwargs):
    traceback.print_exc()


got_request_exception.connect(exception_printer)

call_command('syncdb')
print 'Serving on 8088...'
WSGIServer(('', 8088), WSGIHandler()).serve_forever()
