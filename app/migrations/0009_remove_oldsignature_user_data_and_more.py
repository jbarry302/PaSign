# Generated by Django 4.2.7 on 2023-11-23 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_currentsignature_signature_files_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oldsignature',
            name='user_data',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='signature_type',
        ),
        migrations.DeleteModel(
            name='CurrentSignature',
        ),
        migrations.DeleteModel(
            name='OldSignature',
        ),
    ]