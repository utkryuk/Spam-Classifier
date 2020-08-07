from django import forms

class SpamForm(forms.Form):
    email_body = forms.CharField(
        widget=forms.Textarea(),
        help_text="Write the message here!"
    )
    # source = forms.CharField(
    #     max_length=50,
    #     widget=forms.HiddenInput()
    # )
    
    def clean(self):
        cleaned_data = super(SpamForm, self).clean()
        email_body = cleaned_data.get('email_body')
        if not email_body:
            raise forms.ValidationError('You have to write something!')
    
