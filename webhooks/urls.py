from django.urls import path
from webhooks.views import CovidBotView

urlpatterns = [
    path('', CovidBotView.as_view()),
]
