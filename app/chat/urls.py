from django.urls import path

from app.chat.views import ChatListView, MessageListView

urlpatterns = [
    path('', ChatListView.as_view()),
    path('<int:pk>/message/', MessageListView.as_view()),
]
