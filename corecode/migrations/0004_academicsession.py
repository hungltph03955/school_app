# Generated by Django 3.0.8 on 2020-09-30 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0003_academicterm'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('current', models.BooleanField(default=False, null=True)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
    ]