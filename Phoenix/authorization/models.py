from django.db import models

statuses = (
    ('OK', 'OK'),
    ('BANNED', 'BANNED'),
    ('JUST NEW', 'JUST NEW'),
)
types = (
    ('Admin', 'Admin'),
    ('User', 'User'),
)

class User(models.Model):
    full_name = models.CharField('FullName', max_length = 255)
    contacts = models.TextField('Contacts', max_length = 255)
    birth_date = models.DateTimeField('BirthDate')
    login = models.CharField('Login', max_length = 50)
    password = models.CharField('Password', max_length = 20)
    user_type = models.CharField('UserType', choices = types, default = types[1], max_length = 15)
    user_status_id = models.CharField('UserStatusId', choices = statuses, default = statuses[2], max_length = 15)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Accident(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    accident = models.TextField('Accident', max_length = 1000)
    accident_time = models.DateTimeField('AccidentTime')
    accident_status = models.CharField('Status', max_length = 50)
    accident_comment = models.TextField('Comment', max_length = 255)

    def __str__(self):
        return self.accident

    class Meta:
        verbose_name = 'Accident'
        verbose_name_plural = 'Accidents'