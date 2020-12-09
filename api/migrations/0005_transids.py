# Generated by Django 2.2.12 on 2020-12-09 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_plans'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransIDs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans_num', models.CharField(max_length=30, null=True)),
                ('trans_user', models.CharField(max_length=30, null=True)),
                ('type', models.CharField(max_length=30, null=True)),
                ('reference', models.CharField(max_length=30, null=True)),
                ('version', models.CharField(max_length=30, null=True)),
                ('status', models.CharField(max_length=30, null=True)),
                ('amount', models.CharField(max_length=30, null=True)),
                ('debit', models.CharField(max_length=30, null=True)),
                ('credit', models.CharField(max_length=30, null=True)),
                ('info', models.TextField(blank=True, null=True)),
                ('entity', models.CharField(max_length=30, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'trans_ids',
            },
        ),
    ]
