﻿import os
import sys

root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, 'site-packages.zip'))  

import sae
from alpha import wsgi

application = sae.create_wsgi_app(wsgi.application)