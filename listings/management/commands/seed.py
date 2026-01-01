from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker
import random

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        fake = Faker()
        listings = []

        for _ in range(10):  # Create 10 sample listings
            listing = Listing(
                title=fake.sentence(nb_words=3),
                description=fake.paragraph(),
                price_per_night=round(random.uniform(50, 500), 2),
                location=fake.city()
            )
            listings.append(listing)

        Listing.objects.bulk_create(listings)
        self.stdout.write(self.style.SUCCESS('Successfully seeded listings!'))
