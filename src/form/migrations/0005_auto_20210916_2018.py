# Generated by Django 3.2.7 on 2021-09-16 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_alter_request_num_persons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='coitus',
            field=models.BooleanField(default=False, verbose_name='Is coitus'),
        ),
        migrations.AlterField(
            model_name='request',
            name='sleepover_date_from',
            field=models.DateField(blank=True, null=True, verbose_name='Sleepover date from'),
        ),
        migrations.AlterField(
            model_name='request',
            name='sleepover_date_to',
            field=models.DateField(blank=True, null=True, verbose_name='Sleepover date to'),
        ),
    ]
