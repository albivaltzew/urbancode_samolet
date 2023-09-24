import os
import shutil

source_folder = "/Users/albivaltzew/Desktop/urbanhack-train/augment_repo/Augmentation-using-Albumentations/yolo_ann"  # Replace with the path to your source folder

# Define the paths to the destination folders
image_folder = os.path.join(source_folder, "images")
text_folder = os.path.join(source_folder, "labels")

# Create the destination folders if they don't exist
os.makedirs(image_folder, exist_ok=True)
os.makedirs(text_folder, exist_ok=True)

# Loop through files in the source folder
for filename in os.listdir(source_folder):
    source_file = os.path.join(source_folder, filename)

    if os.path.isfile(source_file):
        # Check the file extension
        file_extension = filename.lower().split('.')[-1]

        if file_extension == "jpg" or file_extension == "JPG":
            # Move jpg files to the images folder
            shutil.copy(source_file, os.path.join(image_folder, filename))
        elif file_extension == "txt":
            # Move txt files to the text folder
            shutil.copy(source_file, os.path.join(text_folder, filename))

print("Files sorted successfully.")
