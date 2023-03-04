from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                              widget=forms.Textarea)

    # Each field type has a default widget that determines how the field is 
    # rendered in HTML.
    