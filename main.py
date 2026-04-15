import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre
from db.models import Actor


def main() -> QuerySet:
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johanson"),
    ]

    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    genres = ["Western", "Action", "Drama"]

    for genre in genres:
        Genre.objects.create(name=genre)

    update_genre = Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")

    update_actor_klooney = Actor.objects.filter(
        last_name="Klooney"
    ).update(last_name="Clooney")

    update_actor_kianu = Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    delete_genre = Genre.objects.filter(name="Action").delete()
    delete_actresses = Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
