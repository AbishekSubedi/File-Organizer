import os
import shutil

# Use a universal path for the Downloads folder
target_folder = os.path.join(os.path.expanduser("~"), "OneDrive\Documents\Desktop")

if not os.path.exists(target_folder):
    print(f"Error: The directory {target_folder} does not exist.")
    exit()

# Get unique file extensions excluding files without an extension
extensions = {
    item.split(".")[-1].lower()  # Convert to lowercase for consistency
    for item in os.listdir(target_folder)
    if os.path.isfile(os.path.join(target_folder, item)) and "." in item
}

# Create folders for each extension type
for extension in extensions:
    folder_path = os.path.join(target_folder, extension)
    if not os.path.exists(folder_path):
        try:
            os.mkdir(folder_path)
        except OSError as e:
            print(f"Error creating folder {folder_path}: {e}")

# Move files to their respective folders
for item in os.listdir(target_folder):
    item_path = os.path.join(target_folder, item)
    if os.path.isfile(item_path) and "." in item:
        file_extension = item.split(".")[-1].lower()
        dest_folder = os.path.join(target_folder, file_extension)
        try:
            shutil.move(item_path, os.path.join(dest_folder, item))
        except shutil.Error as e:
            print(f"Error moving file {item}: {e}")

print("Files organized successfully!")
