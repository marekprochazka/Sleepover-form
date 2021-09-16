from django.urls import path, include

from form.views import SleepOverFormView

app_name = 'form'

urlpatterns = [
    path('', SleepOverFormView.as_view(), name='sleepover_form')
]
