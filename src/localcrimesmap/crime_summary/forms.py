from django import forms

from common.utils import get_month_intervals_as_tuple

RADIUS_CHOICES = (
    (1, ("1 Mile")),
    (2, ("2 Miles")),
    (3, ("5 Miles")),
    (4, ("10 Miles"))
    )

class CrimeSummaryForm(forms.Form):
    lat = forms.FloatField(label='Latitude')
    lng = forms.FloatField(label='Longitude')
    date = forms.ChoiceField(choices = get_month_intervals_as_tuple, label = 'Date')
    radius = forms.ChoiceField(choices = RADIUS_CHOICES, label='Radius', widget=forms.Select())
