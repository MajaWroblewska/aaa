# Generated by Django 4.0.3 on 2022-03-09 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sklepApp', '0045_rename_user_id_koszyk_login_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email',
            old_name='mail',
            new_name='email',
        ),
    ]
