# Generated by Django 3.1.1 on 2020-10-05 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acknowledge', '0009_auto_20201005_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ack_navyinstructionname',
            name='parent',
        ),
        migrations.AlterField(
            model_name='ack_navyinstructionname',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='navyinstruction_name', to='acknowledge.ack_subnavy_instructionssmenu'),
        ),
    ]
