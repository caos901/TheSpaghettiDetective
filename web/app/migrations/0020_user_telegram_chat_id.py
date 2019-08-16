# Generated by Django 2.1.7 on 2019-08-05 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_usercredit'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telegram_secret',
            field=models.CharField(db_index=True, max_length=24, unique=True, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='telegram_chat_id',
            field=models.BigIntegerField(blank=True, null=True),
        )

    ]
