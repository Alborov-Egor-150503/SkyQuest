from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Airline', '0005_auto_20200927_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='address',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='booking',
            name='NumberOfTraveller',
            field=models.IntegerField(default=1),
        ),
    ]
