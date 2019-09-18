from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from MyLogin.models import Myuser


class MainView(TemplateView):
    template_name = 'main_page.html'

    def get(self, request):
        if request.user.authenticated:
            my_user = Myuser.objects.all()
            ctx = {}
            ctx['my_user'] = my_user
            return render(request, self.template_name, ctx)
        else:
            return render(request, self.template_name, {})


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = 'userprofile'

    template_name = 'register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)



