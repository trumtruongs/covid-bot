from django.shortcuts import render
import requests
import re
import redis
import html


def visualization(request):
    r = redis.Redis(host='localhost', port=6379, db=0)
    # result = r.get('visualization')
    # if not r.get('visualization'):
    #     print('new redis cache')
    response = requests.get("https://ncovi.vnpt.vn/views/ncovi_detail.html")
    content = html.unescape(response.content.decode('utf-8'))
    p = r"var\sdataInfo\s\=\s'(.*)';$"
    result = re.search(p, content, re.M).group(1)
    r.set('visualization', result, ex=60)
    return render(request, 'visualization.html', {'data': result })
