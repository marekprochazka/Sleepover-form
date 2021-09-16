from django import forms

from django.conf import settings

from form.models import Request


class SleepoverForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = settings.SLEEPOVER_INPUT_FIELDS
        widgets = {
            'sleepover_date_from': forms.widgets.DateInput(attrs={'type': 'date'}),
            'sleepover_date_to': forms.widgets.DateInput(attrs={'type': 'date'}),
            'estimated_coitus_time_start': forms.widgets.TimeInput(attrs={'type': 'time'}),
            'estimated_coitus_time_end': forms.widgets.TimeInput(attrs={'type': 'time'})
        }
