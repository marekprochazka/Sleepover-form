from django.urls import path
from django.views.generic import TemplateView

app_name = 'infopages'


urlpatterns = [
    path('list', TemplateView.as_view(template_name='infopages/list.html'), name='forms_list')
]