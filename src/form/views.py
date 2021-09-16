from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views import View

from form.forms import SleepoverForm
from form.models import Request


class SleepOverFormView(View):
    def __unzip(self, value):
        if type(value) == list:
            return value[0]
        return value

    def __replace_empty_with_time(self, value):
        return value if value else '00:00'

    def get(self, request):
        form = SleepoverForm()
        return render(request=request, template_name='form/form.html', context={'form': form, 'test': 'test'})

    def post(self, request):
        data = dict(request.POST)
        for key, value in data.items():
            data[key] = self.__unzip(value)
        data['estimated_coitus_time_start'] = self.__replace_empty_with_time(data['estimated_coitus_time_start'])
        data['estimated_coitus_time_end'] = self.__replace_empty_with_time(data['estimated_coitus_time_end'])
        form = SleepoverForm(data)
        valid = form.is_valid()
        if valid and data['num_persons'] != ['0']:
            instance = Request()
            for key, value in data.items():
                if value:
                    setattr(instance, key, self.__unzip(value))
            instance.save()
        return HttpResponseRedirect(reverse('infopages:forms_list'))
