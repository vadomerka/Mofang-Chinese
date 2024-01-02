import sys

import os

INTERP = os.path.expanduser("/var/www/u2141189/data/Project/flaskenv/bin/python")
if sys.executable != INTERP:
   os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())

# from testHtml import app
from main import app
application = app