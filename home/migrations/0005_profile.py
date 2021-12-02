# Generated by Django 3.2 on 2021-11-24 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_delete_myuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='static/images/avt.png', upload_to='static/images/avt/%Y/%m')),
                ('birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('1', 'Female'), ('0', 'Male '), ('2', 'Other ')], default='0', max_length=1)),
                ('bio', models.TextField()),
                ('online', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
