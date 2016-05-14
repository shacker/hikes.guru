try:
    from project.settings_local import *
except ImportError:
    from project.settings_common import *
