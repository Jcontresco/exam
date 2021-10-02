from functools import update_wrapper
from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # agregue claves y valores al diccionario de errores para cada campo no válido
        if len(postData['first_name']) < 3:
            errors["first_name"] = "First name should be at least 3 characters"
        if len(postData['last_name']) < 3:
            errors["last_name"] = "Last name should be at least 3 characters"
        try:
            validate_email(postData['email'])
        except ValidationError:
            print('VALIDATION ERROR')
            errors["email"] = "please enter a valid email"
        # if EmailValidator(postData['email']):
        #     errors["first_name"] = "First name should be at least 5 characters"
        if postData['password'] != postData['confirmed_pw']:
            errors["password"] = "Passwords must be the same"

        return errors
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    objects = UserManager()
    created_at = models.TimeField(auto_now=True)
    updated_at = models.TimeField(auto_now=True)
 