from django.contrib import admin
from .models import User
from .models import Accident

admin.site.register(User)
admin.site.register(Accident)