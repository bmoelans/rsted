import os

# configuration
DEBUG = False  # 'RSTED_PROD' not in os.environ

# Listen IP
# 0.0.0.0   is open to everyone,
# 127.0.0.1 is localhost only.
HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", 5000))


try:
    from settings_local import *  # noqa: F401, F403
except ImportError:
    pass
