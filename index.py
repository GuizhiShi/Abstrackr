__author__ = 'mq20155490'
import sys

from paste.deploy import loadapp
from eventlet import wsgi
import eventlet
#import paste.fixture

app = loadapp('config:/Users/mq20155490/Desktop/CEL/abstrackr_test/test_sample.ini')
listener = eventlet.listen(('', 5050))
pool = eventlet.GreenPool(1000)
wsgi.server(listener, app, custom_pool=pool)