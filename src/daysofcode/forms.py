from django import forms

from .models import DayLog

class DayLogForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget = forms.Textarea)
    day = forms.CharField()
    dayInternal = forms.IntegerField()

class DayLogModelForm(forms.ModelForm):
    class Meta:
        model = DayLog
        fields = ['title', 'content', 'day', 'dayInternal']