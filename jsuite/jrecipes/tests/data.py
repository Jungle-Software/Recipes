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
        nutritional_info="Pretty healthy"
    )

    Recipe.objects.create(
        title="Testerino 2",
        description="The second :^)",
        portion_size=4,
        prep_time=20,
        cook_time=40,
        ingredients="This will be changed!!",
        instructions="Do this, then that.",
        additional_notes="Greasy af",
        nutritional_info="None"
    )

    # Overriding creation date for snapshot testing
    Recipe.objects.filter(title="Test1").update(date_created=datetime.date(2022, 5, 5))
    Recipe.objects.filter(title="Testerino 2").update(date_created=datetime.date(2022, 5, 5))

