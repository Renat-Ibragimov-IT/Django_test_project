from django.core.management.base import BaseCommand
from faker import Faker
from movies_app.models import Movie, Actor
import random


class Command(BaseCommand):
    help = "Add new movie(s) to db"

    def add_arguments(self, parser):
        parser.add_argument('--actors', type=int, default=20)
        parser.add_argument('--movies', type=int, default=10)

    def handle(self, *args, **options):
        faker = Faker()
        for i in range(options['actors']):
            new_actor = Actor(name=faker.name(),
                              dob=faker.date_of_birth())
            new_actor.save()
        for i in range(options['movies']):
            new_movie = Movie(name=" ".join(faker.text().split()
                                            [:random.randint(1, 5)]),
                              description=faker.sentences()[0],
                              release_date=faker.date(),
                              rating=random.randint(1, 10),
                              duration=faker.time())
            new_movie.save()
            actors_count = Actor.objects.count()
            for actor in range(random.randint(5, 10)):
                new_movie.actors.add(random.randint(1, actors_count))
            new_movie.save()





