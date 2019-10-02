# Generated by Django 2.2.1 on 2019-10-02 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_auto_20191002_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='asignee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='planner.Person'),
        ),
        migrations.AlterField(
            model_name='task',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='planner.Schedule'),
        ),
    ]
