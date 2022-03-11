from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        if 'sai' in title.lower():
            raise forms.ValidationError('we don\'t let uruks join our club')