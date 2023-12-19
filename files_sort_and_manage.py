import os
import shutil

# To manage your similar extension files in the same folder
# Just change the target_folder's path
target_folder = "/home/abishek/Downloads"
extensions = {
    item.split(".")[-1]
    for item in os.listdir(target_folder)
    if os.path.isfile(os.path.join(target_folder, item))
}

# Creates folders for each extension types
for extension in extensions:
    if not os.path.exists(os.path.join(target_folder, extension)):
        os.mkdir(os.path.join(target_folder, extension))


# Moves files to their respective folders
for item in os.listdir(target_folder):
    if os.path.isfile(os.path.join(target_folder, item)):
        file_extension = item.split(".")[-1]
        shutil.move(
            os.path.join(target_folder, item),
            os.path.join(target_folder, file_extension, item),
        )
