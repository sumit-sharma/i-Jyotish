# Generated by Django 3.2.6 on 2021-12-26 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFollowing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('following_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following_user_id', to=settings.AUTH_USER_MODEL, verbose_name='followed_by')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_user_id', to=settings.AUTH_USER_MODEL, verbose_name='user_id')),
            ],
            options={
                'verbose_name_plural': 'followers',
                'db_table': 'followers',
                'ordering': ['-created_at'],
            },
        ),
    ]