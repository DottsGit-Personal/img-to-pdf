import os
from img2pdf import convert, ImageOpenError

def jpg_to_pdf(directory, output_file):
    # Get a list of all .jpg files in the directory
    jpg_files = [file for file in os.listdir(directory) if file.lower().endswith('.jpg')]

    processed_files = 0

    # Create a list to store the image file paths
    image_paths = []

    for jpg_file in jpg_files:
        image_path = os.path.join(directory, jpg_file)
        
        try:
            # Validate the image file by opening it
            with open(image_path, 'rb') as file:
                convert(image_path)
                image_paths.append(image_path)
                processed_files += 1
                print(f"Added file: {jpg_file}")
        
        except ImageOpenError:
            print(f"Skipping file: {jpg_file}. Unable to open the image.")
        
        except Exception as e:
            print(f"An error occurred while processing file: {jpg_file}")
            print(f"Error: {str(e)}")

    if processed_files > 0:
        # Convert the images to PDF
        with open(output_file, "wb") as f:
            f.write(convert(image_paths))

        print(f"PDF generation complete. {processed_files} files processed.")
    else:
        print("No valid image files found.")

# Specify the directory containing the .jpg files
directory = './jpg'

# Specify the output PDF file name
output_file = 'combined.pdf'

# Call the function to convert .jpg files to PDF
jpg_to_pdf(directory, output_file)