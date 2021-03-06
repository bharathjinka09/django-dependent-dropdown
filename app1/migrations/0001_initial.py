# Generated by Django 2.2 on 2020-04-10 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subject', models.CharField(choices=[('Computer Science', 'Computer Science'), ('Business', 'Business')], max_length=50)),
                ('job', models.CharField(choices=[('Software Engineer', 'Software Engineer'), ('Data Scientist', 'Data Scientist'), ('Accountant', 'Accountant'), ('Financial Analyst', 'Financial Analyst')], max_length=50)),
            ],
        ),
    ]
