import os

# configuration
DEBUG = 'RSTED_PROD' not in os.environ
RUN_PATH = 'var/run'
PID_FILE = 'fastcgi.pid'
SOCKET_FILE = 'rsted.sock'
FCGI_UMASK = '000'  # you can override this in settings_local.py if you wish

# Listen IP
# 0.0.0.0   is open to everyone,
# 127.0.0.1 is localhost only.
HOST = "0.0.0.0"
PORT = 5000


try:
    from settings_local import *  # noqa: F401, F403
except ImportError:
    pass
