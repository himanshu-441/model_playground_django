# Generated by Django 4.1.7 on 2023-03-23 08:39

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_student_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='slug',
            field=models.CharField(max_length=100, null=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')]),
        ),
    ]
