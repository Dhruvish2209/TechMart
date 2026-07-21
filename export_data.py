import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "electronic_bazaar.settings")
django.setup()

from django.core.management import call_command

with open("data.json", "w", encoding="utf-8") as f:
    call_command(
        "dumpdata",
        exclude=["auth.permission", "contenttypes"],
        indent=2,
        stdout=f,
    )

print("data.json created successfully!")