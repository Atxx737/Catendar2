# Generated by Django 3.2 on 2021-12-01 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('home', '0007_auto_20211126_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
        migrations.AddField(
            model_name='project',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name_project',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task',
            field=models.CharField(max_length=30),
        ),
    ]
