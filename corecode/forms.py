from django import forms
from django.forms import ModelForm, modelformset_factory

from .models import Subject, StudentClass, AcademicTerm, AcademicSession, SiteConfig

SiteConfigForm = modelformset_factory(SiteConfig, fields=('key', 'value',), extra=0)


class SubjectForm(ModelForm):
    prefix = 'Subject'

    class Meta:
        model = Subject
        fields = ['name']


class StudentClassForm(ModelForm):
    prefix = 'Class'

    class Meta:
        model = StudentClass
        fields = ['name']


class AcademicTermForm(ModelForm):
    prefix = 'Academic Term'

    class Meta:
        model = AcademicTerm
        fields = ['name', 'current']


class AcademicSessionForm(ModelForm):
    prefix = 'Academic Session'

    class Meta:
        model = AcademicSession
        fields = ['name', 'current']


class CurrentSessionForm(forms.Form):
    current_session = forms.ModelChoiceField(
        queryset=AcademicSession.objects.all(),
        help_text='Click <a href="/session/create/?next=current-session/">here</a> to add new session'
    )
    current_term = forms.ModelChoiceField(
        queryset=AcademicTerm.objects.all(),
        help_text='Click <a href="/term/create/?next=current-session/">here</a> to add new term'
    )
