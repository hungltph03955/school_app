from django import forms
from django.forms import ModelForm, modelformset_factory

from .models import Subject


class SubjectForm(ModelForm):
    prefix = 'Subject'

    class Meta:
        model = Subject
        fields = ['name']
s