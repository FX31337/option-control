import netrc
from urllib.parse import urlencode
from urllib.request import Request, urlopen

class Provider(object):
    _ready = False
    _provider = None
    _opts = None
    _user = None
    _pass = None
    _host = None

    def __init__(self, provider=None):
        _provider = provider

    def _login(self, url=None, post_fields=None):
        try:
            (self._user, self._pass) = self._get_login_info(self._host)
        except TypeError as err:
            print("ERROR: Credentials are missing.")
        request = Request(url, urlencode(post_fields).encode())
        json = urlopen(request).read().decode()
        print(json)

    def _get_login_info(self, host=None):
        if self._opts.usenetrc:
            return self._get_netrc_login_info(host)
        self._ready = True

    def _get_netrc_login_info(self, machine=None):
        # Get the login details from netrc file.
        username = None
        password = None
        try:
            info = netrc.netrc().authenticators(machine)
            if info is not None:
                username = info[0]
                password = info[2]
            else:
                raise netrc.NetrcParseError('No authenticators for %s' % host)
        except (IOError, netrc.NetrcParseError) as err:
            print('ERROR: Problem with parsing .netrc: %s' % err)
        return username, password

    def set_options(self, opts=None):
        self._opts = opts
