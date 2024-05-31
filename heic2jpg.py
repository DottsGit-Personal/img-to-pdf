import os
from PIL import Image
import pillow_heif

# Specify the folder containing HEIC photos
heic_folder = "./input"

# Specify the output folder for JPG photos
jpg_folder = "./jpg"

# Create the output folder if it doesn't exist
if not os.path.exists(jpg_folder):
    os.makedirs(jpg_folder)

# Iterate over all files in the HEIC folder
for filename in os.listdir(heic_folder):
    if filename.lower().endswith(".heic"):
        # Open the HEIC file using pillow_heif
        heif_file = pillow_heif.read_heif(os.path.join(heic_folder, filename))

        # Convert the primary image to a PIL Image object
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )

        # Generate the output JPG file path
        jpg_filename = os.path.splitext(filename)[0] + ".jpg"
        jpg_path = os.path.join(jpg_folder, jpg_filename)

        # Save the image as JPG
        image.save(jpg_path, "JPEG")

print("HEIC to JPG conversion completed.")