# Generated by Django 2.0.5 on 2019-02-22 21:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=50)),
                ('organization', models.CharField(blank=True, max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('bldgroom', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('account_number', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
