# Generated by Django 4.0.2 on 2022-03-12 17:01

import api.v1.user.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
                ('last_name', models.CharField(blank=True, max_length=255, verbose_name='Фамилия')),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, max_length=255, verbose_name='Отчество')),
                ('role', models.IntegerField(choices=[(0, 'Клиент'), (1, 'Поставщик'), (2, 'Автор'), (3, 'Администратор')], default=0, verbose_name='Рол')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField(auto_now=True, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('phone', models.CharField(blank=True, max_length=12, validators=[api.v1.user.validators.validate_phone], verbose_name='Телефон номер')),
                ('gender', models.IntegerField(choices=[(0, 'Мужчина'), (1, 'Женщина')], default=0, verbose_name='Пол')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Адрес')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]