# Generated by Django 3.0.5 on 2020-04-24 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usersreg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name', models.CharField(max_length=10, verbose_name='User_name')),
                ('user_email', models.EmailField(max_length=30)),
                ('passw', models.CharField(max_length=10, verbose_name='password')),
            ],
        ),
    ]
