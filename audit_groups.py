import tornado.options
import tornado.httpclient
import json

# GET https://www.googleapis.com/admin/directory/v1/groups?domain=domain name
# &customer=my_customer or customerId&pageToken=pagination token
# &maxResults=max results

def run(access_token):
    groups_api_endpoint = "https://www.googleapis.com/admin/directory/v1/groups?domain=%s"
    settings_api_endpoint = "https://www.googleapis.com/groups/v1/groups/%s"
    httpclient = tornado.httpclient.HTTPClient()
    headers = {'Authorization': 'Bearer ' + access_token}

    groups_response = httpclient.fetch(groups_api_endpoint % tornado.options.options.domain, headers=headers)
    assert groups_response.code == 200
    groups = json.loads(groups_response.body)["groups"]
    for group in groups:
        settings = httpclient.fetch(settings_api_endpoint % group["email"], headers=headers)
        print "****" * 10
        print group["email"]
        for line in settings.body.split('\n'):
            if 'apps:whoCanViewGroup' in line:
                print line

if __name__ == "__main__":
    tornado.options.define("access_token")
    tornado.options.define("domain")
    tornado.options.parse_command_line()
    run(tornado.options.options.access_token)