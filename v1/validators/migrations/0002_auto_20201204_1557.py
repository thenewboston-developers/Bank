# Generated by Django 3.1.3 on 2020-12-04 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validators', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='validator',
            name='ip_address',
            field=models.GenericIPAddressField(),
        ),
        migrations.AddIndex(
            model_name='validator',
            index=models.Index(fields=['ip_address', 'port', 'protocol'], name='validators__ip_addr_d18429_idx'),
        ),
        migrations.AddConstraint(
            model_name='validator',
            constraint=models.UniqueConstraint(fields=('ip_address', 'port', 'protocol'), name='validators_validator_unique_ip_port_proto'),
        ),
    ]
