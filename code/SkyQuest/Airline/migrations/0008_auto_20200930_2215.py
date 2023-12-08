from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Airline', '0007_remove_booking_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='price',
            new_name='Price',
        ),
    ]
