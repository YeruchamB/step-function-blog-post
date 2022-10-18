import urllib3


http = urllib3.PoolManager()


def lambda_handler(event, context):
    resp = http.request('GET', 'https://google.com')
    if resp.status != 200:
        print('Huston, we have a problem')
    else:
        print('All quiet on the western front')
