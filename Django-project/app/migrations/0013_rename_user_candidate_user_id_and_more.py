# Generated by Django 4.2.2 on 2023-06-24 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_company_website'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='client',
            new_name='client_id',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='comapany_name',
            new_name='company_name',
        ),
    ]