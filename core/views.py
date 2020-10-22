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


class HomeView(TemplateView):
    """Home page View"""
    template_name = 'home.html'

    def dispatch(self, request, *args, **kwargs):
        """If the user is not logged in - redirect to the registration/authorization page"""
        if not request.user.is_authenticated:
            return redirect('login')
        return super(self.__class__, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['remembers'] = Remember.objects.filter(user=self.request.user)  # Adding memories to the context
        return context


class AddRememberView(CreateView):
    """View adding a new memory"""
    template_name = 'add_remeber_form.html'
    form_class = RememberForm
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        """If the user is not logged in - redirect to the registration/authorization page"""
        if not request.user.is_authenticated:
            return redirect('login')
        return super(self.__class__, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user  # Sending a user to a form
        return super().form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))
