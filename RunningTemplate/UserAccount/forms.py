import csv
from django import forms
from django.contrib.auth.models import User
from models import RunResultsTable


class ImportRunResults(forms.Form):
    select_file_to_upload = forms.FileField(label='Wybierz plik')

    # TODO this method isn't checked yet! So do this!
    def save(self):
        records = csv.reader(self.cleaned_data["select_file_to_upload"], delimiter=';')
        for column in records:
            database_row_object = RunResultsTable()
            database_row_object.runner_id = column[1] # maybe it will be needed to transform it to User object first
            database_row_object.time_5km = column[2]  # TODO converting to double can be needed (for this 2 lines of code)
            database_row_object.time_overall = column[3]
            database_row_object.save()