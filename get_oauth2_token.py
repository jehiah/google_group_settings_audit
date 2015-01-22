'''
    This script will attempt to open your webbrowser,
    perform OAuth 2 authentication and print your access token.

    It depends on two libraries: oauth2client and gflags.

    To install dependencies from PyPI:

    $ pip install python-gflags oauth2client

    Then run this script:

    $ python get_oauth2_token.py
    
    This is a combination of snippets from:
    https://developers.google.com/api-client-library/python/guide/aaa_oauth
'''

from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run
from oauth2client.file import Storage
import tornado.options

if __name__ == "__main__":
    tornado.options.define("client_id")
    tornado.options.define("client_secret")
    tornado.options.parse_command_line()

    flow = OAuth2WebServerFlow(client_id=tornado.options.options.client_id,
                               client_secret=tornado.options.options.client_secret,
                               scope='https://www.googleapis.com/auth/apps.groups.settings https://www.googleapis.com/auth/admin.directory.group.readonly',
                               redirect_uri='http://example.com/auth_return')

    storage = Storage('creds.data')

    credentials = run(flow, storage)

    print "access_token: %s" % credentials.access_token