from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Airline', '0006_auto_20200929_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='phone',
        ),
    ]
