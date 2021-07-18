from django import forms
from . import models


class SearchForm(forms.Form):

    pass

class CreateDiadnosisForm(forms.ModelForm):
    class Meta:
        model = models.Diagnosis
        fields = ('file',)

    def save(self, pk, *args, **kwargs):
        image = super().save(commit=False)
        patient = models.Patient.objects.get(pk=pk)
        image.patient = patient
        image.save()


class CreatePatientForm(forms.ModelForm):

    class Meta:
        model = models.Patient
        fields = [
            "name",
            "id",
            "age",
            "gender",
            "doctor",
            "description",
        ]