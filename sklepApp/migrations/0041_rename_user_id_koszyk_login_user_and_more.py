# Generated by Django 4.0.3 on 2022-03-09 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklepApp', '0040_remove_user_email_id_alter_user_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='koszyk_login',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='adres_id',
            new_name='adres',
        ),
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(max_length=100),
        ),
    ]
