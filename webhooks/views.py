from covidbot import settings
from rest_framework.views import APIView
from django.http.response import HttpResponse
from webhooks import send, receive


class CovidBotView(APIView):
    def get(self, request, format=None):
        mode = self.request.GET['hub.mode']
        token = self.request.GET['hub.verify_token']
        challenge = self.request.GET['hub.challenge']
        if mode and token:
            if token == settings.VERIFY_TOKEN and mode == 'subscribe':
                return HttpResponse(challenge)
        return HttpResponse('Error, invalid token')

    def post(self, request, format=None):
        body = request.data.get('entry')
        entry = body[0]
        messaging_event = entry["messaging"][0]
        sender_id = messaging_event['sender']['id']
        page_id = messaging_event['recipient']['id']
        message = messaging_event.get('message')
        postback = messaging_event.get('postback')
        send.typing_on(sender_id, page_id)
        if message:
            receive.receive_message(sender_id, page_id, message)
        elif postback:
            receive.receive_postback(sender_id, page_id, postback)
        send.typing_off(sender_id, page_id)
        return HttpResponse('Ok')
