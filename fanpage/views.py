import requests
from fanpage.models import Fanpage


def call_send_api(edge, access_token):
    url = 'https://graph.facebook.com/v6.0/{}?access_token={}'.format(edge, access_token)
    result = requests.get(url)
    return result.json()


def get_page_owner(user_id, access_token):
    return call_send_api(
        edge='{}/accounts/'.format(user_id),
        access_token=access_token
    )


def insert_page_by_client(access_token):
    pages_info = get_page_owner('me', access_token)
    if pages_info.get('error'):
        return print(pages_info.get('error')['message'])
    fanpages = []
    for page in pages_info['data']:
        fanpage = Fanpage(
            id=page['id'],
            name=page['name'],
            access_token=page['access_token']
        )
        fanpage.save()
        fanpages.append(fanpage)

    return fanpages
