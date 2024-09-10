# Generated by Django 4.2.7 on 2024-01-19 04:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0005_alter_enrollment_portal_screenshot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='portal_screenshot',
            field=models.FileField(upload_to='portal_screenshot/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'gif', 'heif', 'heic'])]),
        ),
    ]
