from django import forms

class FormUpload(forms.Form):
    """
    Form where the file will be uploaded
    """
    file_field = forms.FileField(label='lbl_file')