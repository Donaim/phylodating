# Generated by Django 2.1.10 on 2020-04-21 21:54

from django.db import migrations, models
import tools.phylodating.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=200)),
                ('job_id', models.IntegerField(default=tools.phylodating.models.generate_job_id)),
                ('info_csv', models.FileField(upload_to=tools.phylodating.models.upload_callback_info_csv)),
                ('unrooted_tree', models.FileField(upload_to=tools.phylodating.models.upload_callback_unrooted_tree)),
                ('rooted_tree_out', models.FileField(upload_to=tools.phylodating.models.upload_callback_rooted_tree)),
                ('data_out', models.FileField(upload_to=tools.phylodating.models.upload_callback_data_file)),
                ('stats_out', models.FileField(upload_to=tools.phylodating.models.upload_callback_stats_file)),
                ('plot', models.ImageField(upload_to=tools.phylodating.models.upload_callback_plot_file)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('N', 'Not Run'), ('R', 'Running'), ('S', 'Successful'), ('F', 'Failed'), ('K', 'Killed')], default='N', max_length=1)),
                ('stdout', models.TextField()),
                ('stderr', models.TextField()),
                ('cmd', models.TextField(blank=True)),
            ],
        ),
    ]
