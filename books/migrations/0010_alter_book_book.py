# Generated by Django 4.1.3 on 2022-12-01 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_alter_book_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book',
            field=models.FileField(blank=True, editable=False, null=True, upload_to='uploads/'),
        ),
    ]
