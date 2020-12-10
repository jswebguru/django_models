# Generated by Django 2.2.12 on 2020-12-09 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_transtypes'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_id', models.CharField(max_length=30, null=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('title', models.CharField(max_length=30, null=True)),
                ('type', models.CharField(max_length=30, null=True)),
                ('value', models.CharField(max_length=30, null=True)),
                ('location', models.CharField(max_length=30, null=True)),
                ('info', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'contact_info',
            },
        ),
    ]