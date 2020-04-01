from django.urls import path
from webhooks.hooks import CovidBotView

urlpatterns = [
    path('', CovidBotView.as_view()),
]
