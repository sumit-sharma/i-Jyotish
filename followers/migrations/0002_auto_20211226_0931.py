# Generated by Django 3.2.6 on 2021-12-26 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('followers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfollowing',
            name='following_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userfollowing',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_user_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
