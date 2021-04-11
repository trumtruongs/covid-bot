from rest_framework.views import APIView
from fanpage.views import insert_page_by_client
from client.models import Client


class ClientView(APIView):
    def post(self, request, format=None):
        access_token = request['body'].get('access_token')
        client = Client(request['body'])
        client.save()
        fanpages = insert_page_by_client(access_token)
        client.pages.set(fanpages)
