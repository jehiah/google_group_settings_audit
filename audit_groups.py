from oauth2client.client import OAuth2WebServerFlow
from oauth2client import tools
from oauth2client.file import Storage
import tornado.options
import tornado.httpclient
import json

# GET https://www.googleapis.com/admin/directory/v1/groups?domain=domain name
# &customer=my_customer or customerId&pageToken=pagination token
# &maxResults=max results

def get_access_token(client_id, client_secret):
    '''
        This script will attempt to open your webbrowser,
        perform OAuth 2 authentication and print your access token.

        It depends on two libraries: oauth2client and gflags.

        To install dependencies from PyPI:

        $ pip install python-gflags oauth2client

        Then run this script with --client-id=.. and --client-secret=...
    
        This is a combination of snippets from:
        https://developers.google.com/api-client-library/python/guide/aaa_oauth
    '''
    
    assert client_id
    assert client_secret

    flow = OAuth2WebServerFlow(client_id=client_id,
                               client_secret=client_secret,
                               scope='https://www.googleapis.com/auth/apps.groups.settings https://www.googleapis.com/auth/admin.directory.group.readonly',
                               redirect_uri='http://example.com/auth_return')

    storage = Storage('creds.data')

    credentials = tools.run(flow, storage)
    return credentials.access_token

def run(access_token, domain, filter_key):
    assert access_token
    assert domain
    
    groups_api_endpoint = "https://www.googleapis.com/admin/directory/v1/groups?domain=%s"
    settings_api_endpoint = "https://www.googleapis.com/groups/v1/groups/%s"
    httpclient = tornado.httpclient.HTTPClient()
    headers = {'Authorization': 'Bearer ' + access_token}

    groups_response = httpclient.fetch(groups_api_endpoint % domain, headers=headers)
    assert groups_response.code == 200
    groups = json.loads(groups_response.body)["groups"]
    for group in groups:
        settings = httpclient.fetch(settings_api_endpoint % group["email"], headers=headers)
        print "****" * 10
        print group["email"]
        if filter_key:
            for line in settings.body.split('\n'):
                if filter_key in line:
                    print line
        else:
            print settings.body

if __name__ == "__main__":
    tornado.options.define("client_id")
    tornado.options.define("client_secret")
    tornado.options.define("access_token")
    tornado.options.define("domain")
    tornado.options.define("key", default="", help="filter to only the following group value (ie: whoCanViewGroup)")
    tornado.options.parse_command_line()
    
    o = tornado.options.options
    
    access_token = o.access_token
    if not access_token:
        access_token=get_access_token(o.client_id, o.client_secret)
    
    run(access_token, o.domain, o.key)