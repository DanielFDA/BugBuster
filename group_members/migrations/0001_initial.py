# Generated by Django 3.1.5 on 2021-01-28 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('manager', 'Manager'), ('developer', 'Developer')], default='developer', max_length=15)),
            ],
        ),
    ]
