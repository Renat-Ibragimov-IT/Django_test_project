# Generated by Django 4.0.5 on 2022-06-13 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0002_alter_actor_name_alter_movie_name_alter_movie_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='vote',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(choices=[(0, 'Fuck NO!'), (1, 'Horrible'), (2, 'Terrible'), (3, 'Lousy'), (4, 'Crummy'), (5, 'OK'), (6, 'Pretty Good'), (7, 'Good'), (8, 'Great'), (9, 'Excellent'), (10, 'Fabulous')], db_index=True),
        ),
    ]
