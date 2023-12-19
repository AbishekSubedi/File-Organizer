File Organizer



This simple Python script helps you organize files in a specified folder based on their file extensions. It scans a target folder for files, categorizes them by their extensions, and moves them into subfolders named after their respective extensions.


How to Use:

1. Open the script in a text editor or integrated development environment (IDE) of your choice.

2. Modify the target_folder variable to specify the path of the folder containing the files you want to organize.

        target_folder = "/path/to/your/target/folder"

3. Run the script in terminal or bash.

        python3 file_organizer.py

  Make sure you have the necessary permissions to read from and write to the specified target folder.

4. The script will create subfolders for each unique file extension found in the target folder and move the corresponding files into their respective subfolders.


Example:

For instance, if your target folder is "/home/abishek/Downloads" and contains files like "document.txt," "image.jpg," and "data.csv," the script will create subfolders named "txt," "jpg," and "csv" and move the files into their corresponding folders.

    /home/abishek/Downloads
    |-- txt
    |   |-- document.txt
    |-- jpg
    |   |-- image.jpg
    |-- csv
    |   |-- data.csv


Notes:

1. The script uses the shutil.move function to relocate the files. If you encounter any issues related to permissions or file access, make sure you have the necessary rights.

2. If a subfolder for a specific extension already exists, the script will not create a duplicate; it will move the files into the existing subfolder.

3. This script is a basic file organizer and can be extended or modified based on your specific needs.

Feel free to adapt the script to suit your requirements, and happy organizing!
