from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='FullName')),
                ('contacts', models.TextField(max_length=255, verbose_name='Contacts')),
                ('birth_date', models.DateTimeField(verbose_name='BirthDate')),
                ('login', models.CharField(max_length=50, verbose_name='Login')),
                ('password', models.CharField(max_length=20, verbose_name='Password')),
                ('user_type', models.CharField(max_length=15, verbose_name='UserType')),
                ('user_status_id', models.IntegerField(default=0, verbose_name='UserStatusId')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Accident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accident', models.TextField(max_length=1000, verbose_name='Accident')),
                ('accident_time', models.DateTimeField(verbose_name='AccidentTime')),
                ('accident_status', models.CharField(max_length=50, verbose_name='Status')),
                ('accident_comment', models.TextField(max_length=255, verbose_name='Comment')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='authorization.user')),
            ],
            options={
                'verbose_name': 'Accident',
                'verbose_name_plural': 'Accidents',
            },
        ),
    ]
