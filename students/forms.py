from django import forms
from .models import StudentRecord


class AddRecord(forms.ModelForm):
    """Adding student record form"""

    first_name = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "First Name", "class": "form-control"}
        ),
        label="",
    )
    last_name = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Last Name", "class": "form-control"}
        ),
        label="",
    )
    email = forms.EmailField(
        required=True,
        max_length=100,
        widget=forms.widgets.EmailInput(
            attrs={"placeholder": "Email", "class": "form-control"}
        ),
        label="",
    )
    course = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Course", "class": "form-control"}
        ),
        label="",
    )
    gpa = forms.FloatField(
        required=True,
        widget=forms.widgets.NumberInput(
            attrs={"placeholder": "Gpa", "class": "form-control"}
        ),
        label="",
    )

    class Meta:
        """including database model"""

        model = StudentRecord
        exclude = ("user",)
