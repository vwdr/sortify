import os
import shutil
import time

# Folder paths
download_folder = 'C:\path\to\your\folder'
main_folder = 'C:\path\to\your\folder'

# Function to create folder if it doesn't exist
def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Function to move image to its corresponding folder
def organize_image(image_path):
    # Get file extension
    file_extension = os.path.splitext(image_path)[1].lower()
    
    # Get destination folder path
    dest_folder = os.path.join(main_folder, file_extension[1:])
    
    # Create destination folder if it doesn't exist
    create_folder(dest_folder)
    
    # Move image to destination folder
    shutil.move(image_path, dest_folder)

# Continuously check for new images
while True:
    # Get list of all files in the download folder
    all_files = os.listdir(download_folder)
    
    # Filter out non-image files
    image_files = [file for file in all_files if os.path.splitext(file)[1].lower() in ['.jpg', '.jpeg', '.png']]
    
    # Organize each image file
    for image_file in image_files:
        organize_image(os.path.join(download_folder, image_file))
    
    # Wait for 10 seconds before checking again
    time.sleep(10)
