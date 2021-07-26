from django import forms

from directory.models import Subject

SUBJECTS = [(subject, subject) for
            subject in
            Subject.objects.values_list(
                "subject_name",
                flat=True)]


class SearchForm(forms.Form):
    first_letter_of_last_name = forms.CharField(required=False,
                                                label='First letter of Last Name')
    subject = forms.ChoiceField(label="Subject", required=False,

                                choices=[('', '---------')] +
                                        [(subject, subject) for
                                         subject in
                                         Subject.objects.values_list(
                                             "subject_name",
                                             flat=True)])


class BulkUploadForm(forms.Form):
    csv_file = forms.FileField(label="CSV-file with the list of teachers",
                               widget=forms.FileInput(attrs={'accept': '.csv'}))
    images_archive = forms.FileField(label="ZIP-file with the profile pictures",
                                     widget=forms.FileInput(
                                         attrs={'accept': '.zip'}))
