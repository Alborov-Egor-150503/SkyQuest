from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Airline', '0009_auto_20201206_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightdetail',
            name='ArrivalTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
