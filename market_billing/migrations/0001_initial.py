
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinalBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemID', models.CharField(max_length=10)),
                ('discountID', models.CharField(max_length=10)),
                ('itemName', models.CharField(max_length=25)),
                ('itemPrice', models.FloatField()),
                ('itemCount', models.IntegerField()),
            ],
        ),
    ]
