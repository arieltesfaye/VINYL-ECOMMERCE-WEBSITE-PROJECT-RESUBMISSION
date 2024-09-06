import os
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Load album data'

    def handle(self, *args, **options):
        # Use the correct directory for your album covers
        album_covers_dir = r'C:\Users\hp240\vinyl_store\shop\static\shop\images\album_covers'

        # Check if the directory exists
        if not os.path.exists(album_covers_dir):
            self.stdout.write(self.style.ERROR(f"Directory not found: {album_covers_dir}"))
            return

        # Now proceed with your code to load albums
        for filename in os.listdir(album_covers_dir):
            # your logic for handling album covers
            self.stdout.write(self.style.SUCCESS(f"Processing file: {filename}"))
