from django.shortcuts import render
import requests
import re
import redis
import html

from covidbot import settings


def visualization(request):
    r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)
    response = requests.get("https://ncovi.vnpt.vn/views/ncovi_detail.html")
    content = html.unescape(response.content.decode('utf-8'))
    p = r"var\sdataInfo\s\=\s'(.*)';$"
    result = re.search(p, content, re.M).group(1)
    r.set('visualization', result, ex=60)
    return render(request, 'visualization.html', {'data': result })
