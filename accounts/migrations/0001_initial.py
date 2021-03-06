# Generated by Django 2.2.7 on 2019-11-06 11:08

from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=120, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username must be alphanumeric', regex='^[a-zA-Z0-9.@+-]*$')])),
                ('name', models.CharField(max_length=120)),
                ('rollno', models.CharField(max_length=120, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_rollno', message='Sahi Roll Number Daalo !!', regex='^[0-9]*$')])),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('branch', models.CharField(choices=[('CSE', 'B.Tech.- Comp. Sc. & Engg.'), ('ELECCOMM', 'B.Tech.- Elec. & Comm. Engg.'), ('MECHANICAL', 'B.Tech.- Mechanical Engg.'), ('ELECTRICAL', 'B.Tech.- Electrical Engg.'), ('IT', 'B.Tech.- Information Technology'), ('BBA', 'BBA'), ('BCA', 'BCA'), ('MBA', 'MBA'), ('MCA', 'MCA'), ('MCSE', 'M.Tech.- Comp. Sc. & Engg.'), ('MELECCOMM', 'M.Tech.- Elec. & Comm. Engg.')], default='CSE', max_length=200)),
                ('semester', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], default='6', max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilepic', models.ImageField(upload_to='profilepics')),
                ('user', models.OneToOneField(on_delete=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
