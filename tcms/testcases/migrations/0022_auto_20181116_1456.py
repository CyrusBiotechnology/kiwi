# Generated by Django 2.1.1 on 2018-11-16 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testcases', '0021_convert_cc_list_to_string'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicaltestcase',
            name='requirement',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='requirement',
        ),
    ]
