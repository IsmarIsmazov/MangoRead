from rest_framework.exceptions import ValidationError


def validate_password(value):
    if len(value) < 6 or len(value) > 20:
        raise ValidationError("Password must be between 6 and 20 characters long.")
    return value