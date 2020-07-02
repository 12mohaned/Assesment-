# Generated by Django 3.0.3 on 2020-07-02 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blog', '0004_auto_20200702_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Comment', models.CharField(max_length=50)),
                ('Content', models.TextField()),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.Post')),
                ('Postuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
