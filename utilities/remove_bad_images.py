"""
Author: Andrew Higgins
https://github.com/speckly

simple utility to remove bad images
"""

import os
from PIL import Image
from sys import argv

def remove_corrupt_images(directory):
    # Ensure the directory exists
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
        return

    # List all files in the directory
    files = os.listdir(directory)
    jpg_files = [file for file in files if file.lower().endswith('.jpeg')]

    for file in jpg_files:
        file_path = os.path.join(directory, file)
        try:
            # Attempt to open the image file
            with Image.open(file_path) as img:
                img.verify()
        except (IOError, SyntaxError) as e:
            # If an error occurs, the image is corrupt or cannot be opened
            print(f"Removing corrupt image: {file}")
            os.remove(file_path)

if __name__ == "__main__":
    directory = f'../images/{input("Input images directory: ") if len(argv) == 1 else argv[1]}'
    remove_corrupt_images(directory)
