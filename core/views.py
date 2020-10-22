from django.shortcuts import redirect
from django.views.generic import CreateView
from django.views.generic.base import TemplateView

from core.forms import RememberForm
from core.models import Remember


class LoginView(TemplateView):
    """View The Registration/Authorization"""
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        """If the user is logged in redirect to the home page"""
        if request.user.is_authenticated:
            return redirect('home')
        return super(self.__class__, self).dispatch(request, *args, **kwargs)

