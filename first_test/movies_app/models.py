from django.db import models


class Movie(models.Model):
    RATE = (
        (0, 'Fuck NO!'),
        (1, 'Horrible'),
        (2, 'Terrible'),
        (3, 'Lousy'),
        (4, 'Crummy'),
        (5, 'OK'),
        (6, 'Pretty Good'),
        (7, 'Good'),
        (8, 'Great'),
        (9, 'Excellent'),
        (10, 'Fabulous'),
    )
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.IntegerField(choices=RATE, db_index=True)
    duration = models.TimeField()
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    dob = models.DateField()
    movies = models.ManyToManyField(Movie, related_name='actors')

    def __str__(self):
        return self.name

