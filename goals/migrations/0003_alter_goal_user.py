# Generated by Django 4.1.3 on 2023-03-20 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('goals', '0002_alter_goal_actions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.student'),
        ),
    ]