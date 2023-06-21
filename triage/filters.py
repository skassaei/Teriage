import django_filters
from .models import *
class TriageFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(label='نام', lookup_expr='icontains')
    last_name = django_filters.CharFilter(label='نام خانوادگی', lookup_expr='icontains')
    gender = django_filters.ChoiceFilter(choices = Triage.gender_choices,label='جنسیت')
    age = django_filters.NumberFilter(label='سن',)
    age__gt = django_filters.NumberFilter(field_name='age',lookup_expr='gt', label="سن بیشتر از")
    age__lt = django_filters.NumberFilter(field_name='age',lookup_expr='lt',label="سن کمتر از")
    level_of_triage = django_filters.CharFilter(label='سطح تریاژ')
    level_of_triage__gt = django_filters.CharFilter(field_name='level_of_triage',lookup_expr='gt', label='سطح تریاژ بیشتر از')
    level_of_triage__lt = django_filters.CharFilter(field_name='level_of_triage',lookup_expr='lt', label='سطح تریاژ کمتر از')



    class Meta:
        model = Triage
        fields = []