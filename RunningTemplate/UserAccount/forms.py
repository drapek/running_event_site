# -*- coding: utf-8 -*-
import csv
from django import forms
from django.contrib.auth.models import User
from models import RunResultsTable
from django.core.exceptions import ObjectDoesNotExist

class ImportRunResults(forms.Form):
    select_file_to_upload = forms.FileField(label='Wybierz plik')

    # TODO this method isn't checked yet! So do this!
    @property
    def save(self):
        error_log = "" # tuple to store information about not

        records = csv.reader(self.cleaned_data["select_file_to_upload"], delimiter=';')
        for column in records:
            database_row_object = RunResultsTable()
            try:
                user = User.objects.get(id=int(column[0]))
                database_row_object.runner_id = user
                database_row_object.time_5km = column[1]  # TODO converting to double can be needed (for this 2 lines of code)
                database_row_object.time_overall = column[2]
                database_row_object.save()

            except ObjectDoesNotExist as e:
                error_log = error_log + "Użytkownik o id" + str(column[0]) + " nie istnieje w bazie użytkowników! Linia " + str(records.line_num) + " pliku CSV \n"
                continue
            except Exception as e:
                error_log = error_log + "Wystąpił nieoczekiwany błąd z id użytkownika. Linia " + str(records.line_num) + " pliku CSV\n"
                continue

            return error_log