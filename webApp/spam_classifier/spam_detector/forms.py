from django import forms

class SpamForm(forms.Form):
    email_body = forms.CharField(
        widget=forms.Textarea(attrs={"rows":8,'placeholder':'Copy your email here...'}),
        help_text="Write the email here!",
    )

    
    def clean(self):
        cleaned_data = super(SpamForm, self).clean()
        email_body = cleaned_data.get('email_body')
        if not email_body:
            raise forms.ValidationError('You have to write something!')
    
