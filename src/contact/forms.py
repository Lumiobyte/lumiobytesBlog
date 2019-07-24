from django import forms

from .models import ContactRequests

class ContactForm(forms.Form):

    fullName = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget = forms.Textarea)

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')

        return email

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactRequests
        fields = ['name', 'email', 'content']

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')

        return email