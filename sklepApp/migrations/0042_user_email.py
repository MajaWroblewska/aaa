# Generated by Django 4.0.3 on 2022-03-09 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sklepApp', '0041_rename_user_id_koszyk_login_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sklepApp.email'),
        ),
    ]
