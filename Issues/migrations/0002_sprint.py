# Generated by Django 2.1.7 on 2019-02-26 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0001_initial'),
        ('Issues', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_sprint', to='Project.Project')),
            ],
        ),
    ]
