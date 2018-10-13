from django import forms


class ReviewForm(forms.Form):
    rating = forms.IntegerField(min_value=0, max_value=5)
    opinion = forms.CharField(widget=forms.Textarea({'cols': '40', 'rows': '5'}), required=False)
