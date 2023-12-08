from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Airline', '0004_auto_20200927_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flightdetail',
            name='NumberOfTraveller',
        ),
        migrations.AddField(
            model_name='booking',
            name='NumberOfTraveller',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
