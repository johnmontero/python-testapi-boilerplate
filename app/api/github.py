import requests

class GithubApi(object):

    def __init__(self, base_url, headers = None):
        self.headers = { 'cache-control': 'no-cache'}

        if headers is not None:
            if not 'cache-control' in sorted(headers):
                headers.update(self.headers)

        self.headers = headers
        self.base_url = base_url

    def get_user(self):

        r = requests.get('{}/user'.format(
            self.base_url), headers=self.headers)

        return r