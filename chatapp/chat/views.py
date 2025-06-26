from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render, redirect

class LoginView(View):
    template_name = 'chat/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        request.session['username'] = username
        return redirect('chat')


class ChatView(TemplateView):

    def get(self, request, *args, **kwargs):
        username = request.session.get('username')
        if not username:
            return redirect('login')
        return render(request, 'chat/chat.html', {'username': username})
