# Generated by Django 4.0 on 2022-07-01 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Password_Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('logo', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
