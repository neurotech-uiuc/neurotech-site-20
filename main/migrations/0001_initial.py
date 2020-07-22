# Generated by Django 3.0.5 on 2020-07-13 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='filler_avatar.png', null=True, upload_to='')),
                ('lead', models.BooleanField(default=False)),
                ('team', models.CharField(choices=[('Software', 'Software'), ('Hardware', 'Hardware'), ('Research', 'Research'), ('Outreach', 'Outreach')], max_length=200, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]