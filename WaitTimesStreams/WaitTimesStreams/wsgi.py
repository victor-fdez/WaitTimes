"""
WSGI config for WaitTimesStreams project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

activate_this = '/home/chingaman/public_html/android/WaitTimes/VirtualPython/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
import pdb
#pdb.set_trace()
import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WaitTimesStreams.settings")
#print >> os.environ['wsgi.errors'], "application debug #1"
#f = open('myfile','w')
#f.write('hello')
#f.close()
#print >> sys.stderr, "application debug #2"
#sys.stderr.write(' '.join(sys.path))
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

#path = '/home/chingaman/public_html/android/WaitTimes/WaitTimesStreams/WaitTimesStreams/'
#if path not in sys.path:
#    sys.path.append(path)
