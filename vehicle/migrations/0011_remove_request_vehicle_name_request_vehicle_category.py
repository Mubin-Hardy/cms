# Generated by Django 4.0.5 on 2022-06-19 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0010_alter_request_category_alter_request_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='vehicle_name',
        ),
        migrations.AddField(
            model_name='request',
            name='vehicle_category',
            field=models.CharField(choices=[('Alappuzha', 'Alappuzha'), ('Wayanad', 'Wayanad'), ('Ernakulam', 'Ernakulam'), ('Thrissur', 'Thrissur'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Pathanamthitta', 'Pathanamthitta'), ('Palakkad', 'Palakkad'), ('Malappuram', 'Malappuram'), ('Kozhikode', 'Kozhikode'), ('Kottayam', 'Kottayam'), ('Kollam', 'Kollam'), ('Kasaragod', 'Kasaragod'), ('Kannur', 'Kannur'), ('Idukki', 'Idukki')], default='thrissur', max_length=50),
            preserve_default=False,
        ),
    ]
