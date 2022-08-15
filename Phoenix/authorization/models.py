from django.db import models

class User(models.Model):
    full_name = models.CharField('FullName', max_length = 255)
    contacts = models.TextField('Contacts', max_length = 255)
    birth_date = models.DateTimeField('BirthDate')
    login = models.CharField('Login', max_length = 50)
    password = models.CharField('Password', max_length = 20)
    user_type = models.CharField('UserType', max_length = 15)
    user_status_id = models.IntegerField('UserStatusId', default = 0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
