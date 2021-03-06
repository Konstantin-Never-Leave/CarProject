from django.shortcuts import render
from django.views.generic import ListView


class HomePage(ListView):
    template_name = 'homepage/homepage.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Cars page")

        return dict(list(context.items()) + list(c_def.items()))
