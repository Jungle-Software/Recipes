import datetime

from ..models import Recipe


def insert_data():
    Recipe.objects.create(
        title="Test1",
        description="My first test!",
        portion_size=4,
        prep_time=20,
        cook_time=40,
        ingredients="This will be changed!!",
        instructions="Do this, then that.",
        additional_notes="Pretty tasty",
        nutritional_info="Pretty healthy",
        date_created=datetime.date(2022, 6, 5)
    )
