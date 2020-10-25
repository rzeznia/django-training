from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

def validate_mass(value):
    if value > 120:
        raise ValidationError("Ważysz więcej niż 120kg, jesteś za gruby do bazy danych")

