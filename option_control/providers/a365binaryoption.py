from option_control.provider import Provider

class a365binaryoptionProvider(Provider):
    _host = '365binaryoption.com'
    _login_uri = 'login'

    def authenticate(self):
        url = "/".join([self._host, self._login_uri])
        print(url)
        post_fields = {'user': 'USER', 'password': 'PASS'}
        self._login('http://' + url, post_fields)
