# Generated by Django 2.2.1 on 2019-05-30 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('username', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45)),
                ('travelStart', models.DateTimeField()),
                ('travelEnd', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='myapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='myapp.Trip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='myapp.User')),
            ],
        ),
    ]
