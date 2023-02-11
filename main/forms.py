from django import forms


class SearchPostals(forms.Form):
    postal_code = forms.CharField(label="Postal Code", max_length=10)
