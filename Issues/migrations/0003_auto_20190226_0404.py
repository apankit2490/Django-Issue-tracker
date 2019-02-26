# Generated by Django 2.1.7 on 2019-02-26 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Issues', '0002_auto_20190226_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issues',
            name='issue_type',
            field=models.CharField(choices=[('TK', 'Task'), ('ST', 'Story'), ('BG', 'Bug'), ('EP', 'Epic')], default='TK', max_length=2),
        ),
    ]
