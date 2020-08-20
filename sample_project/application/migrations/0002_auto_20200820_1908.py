# Generated by Django 3.1 on 2020-08-20 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teamstructure',
            old_name='file',
            new_name='logoUri',
        ),
        migrations.AddField(
            model_name='teamstructure',
            name='club_state',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='TeamPlayerStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('firstname', models.CharField(max_length=200, unique=True)),
                ('identifier', models.CharField(max_length=200)),
                ('club', models.CharField(max_length=200)),
                ('imageUri', models.FileField(blank=True, null=True, upload_to='team/player_image/')),
                ('Player_jersey_number', models.IntegerField(blank=True, null=True)),
                ('country', models.CharField(max_length=200)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teamstructure', to='application.teamstructure')),
            ],
        ),
    ]
