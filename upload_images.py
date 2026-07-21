import os
import cloudinary
import cloudinary.uploader
from decouple import config

# Configure Cloudinary
cloudinary.config(
    cloud_name=config("CLOUDINARY_CLOUD_NAME"),
    api_key=config("CLOUDINARY_API_KEY"),
    api_secret=config("CLOUDINARY_API_SECRET"),
)

MEDIA_FOLDER = "media"

for root, dirs, files in os.walk(MEDIA_FOLDER):
    for file in files:
        if file.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".gif")):
            file_path = os.path.join(root, file)

            # Example:
            # media/photos/products/mobile.jpg
            # becomes:
            # photos/products/mobile
            public_id = os.path.splitext(
                os.path.relpath(file_path, MEDIA_FOLDER)
            )[0].replace("\\", "/")

            print(f"Uploading {public_id}...")

            cloudinary.uploader.upload(
                file_path,
                public_id=public_id,
                overwrite=True,
            )

print("\n✅ All images uploaded successfully!")