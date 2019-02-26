# Generated by Django 2.1.7 on 2019-02-26 09:26

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Project', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('issue_type', models.CharField(choices=[('TK', 'Task'), ('ST', 'Story'), ('BG', 'Bug'), ('EP', 'Epic')], default='TK', max_length=2)),
                ('summary', models.CharField(max_length=30, null=True)),
                ('priority', models.CharField(choices=[('HGH', 'Highest'), ('HG', 'High'), ('MD', 'Medium'), ('LW', 'Low'), ('LWW', 'Lowest')], default='MD', max_length=2, null=True)),
                ('labels', models.CharField(max_length=30, null=True)),
                ('assignee', models.ForeignKey(default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='Project.Project')),
            ],
        ),
    ]
