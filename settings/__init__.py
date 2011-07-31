from base import *

try:
  from local import *
except ImportError:
  pass

try:
  from dev import *
except ImportError:
  pass
