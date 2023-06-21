from django import forms
from django.forms import ModelForm
from .models import Triage
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget


# create a venue form
class TriageForm(ModelForm):
    class Meta:  # this is Not a python code this is for django and this is just how it works we don't know what Meta is doing just add it :\

        # Defineing the table you want to work on
        model = Triage
        fields = "__all__"  # Get all the fields in the table

        # Dictionary for giving our fileds the class of "form control" Bootstrap
        # Can we get ride of the labels we need place holders
        widgets = {
            "admintion_date": AdminDateWidget(),
            "admintion_time": AdminTimeWidget(),
        }