# Generated by Django 4.0.1 on 2022-02-26 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='darte_enregistrement',
            new_name='date_enregistrement',
        ),
    ]