from django import forms

from .widgets import AjaxInputWidget
from django.forms.widgets import SelectDateWidget
from .models import City


class SearchTicket(forms.Form):
    departure = forms.CharField(
        widget=AjaxInputWidget('api/city_ajax',
        attrs={'class': 'inline right-margin'}),
        label='Город отправления'
        )
    destination = forms.CharField(
        widget=AjaxInputWidget('api/city_ajax',
        attrs={'class': 'inline right-margin'}),
        label='Город прибытия'
        )
    date_departure = forms.DateField(
        widget=SelectDateWidget(),
        label='Дата'
        )
