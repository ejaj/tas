# Generated by Django 2.2.7 on 2021-02-27 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0002_agentuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentuser',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Agent'),
        ),
    ]
