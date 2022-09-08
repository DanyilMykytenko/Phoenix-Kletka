from .models import User, Accident
from django import forms

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["full_name", "contacts", "birth_date", "login", "password", "user_type", "user_status_id"]

class AccidentForm(ModelForm):
    class Meta:
        model = Accident
        fields = ["user_id", "accident", "accident_time", "accident_status", "accident_comment"]