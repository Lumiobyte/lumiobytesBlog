from django import forms

from .models import BlogPost

class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget = forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'image', 'content']

    def clean_title(self, *args, **kwargs):
        instance = self.instance

        title = self.cleaned_data.get('title')

        qs = BlogPost.objects.filter(title__iexact = title) # gets a filtered qeuryset containg either nothing or a post with an exactly matching title
        if instance is not None: # if instance (i think that's if an object already exists) is not none a.k.a there is an instance that exists...
            qs = qs.exclude(id = instance.id) # exclude it from the queryset we got to pass the title dupe check when editing a post.

        if qs.exists(): # if there's something in the post...
            raise forms.ValidationError("Title already used!") # throw an error.

        return title # otherwise, send the title back. all is fine!!