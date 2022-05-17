
from django.utils import timezone
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import UserVsTicker
from ticker.tasks import task_ticker_update_all


class IndexListView(LoginRequiredMixin, ListView):
    template_name = 'core/index.html'
    login_url = reverse_lazy('login')
    model = UserVsTicker
    context_object_name = 'objects'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs).filter(user=self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        if self.request.user.is_superuser:
            from ticker.tasks import task_list_ticker
            task_list_ticker()

        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get(self, request, *args, **kwargs):

        return super().get(request, *args, **kwargs)
