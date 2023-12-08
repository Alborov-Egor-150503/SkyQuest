from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Airline', '0010_auto_20201206_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='BookingId',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
