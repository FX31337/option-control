class Provider(object):
    _ready = False

    def _get_login_info(self):
        self._ready = True
