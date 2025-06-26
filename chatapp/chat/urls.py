from django.urls import path
from .views import LoginView, ChatView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('chat/', ChatView.as_view(), name='chat'),
]
