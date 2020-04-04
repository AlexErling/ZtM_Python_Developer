# Two arguments, folder to process, folder to dump

from PIL import Image, ImageFilter
import sys
import os

if __name__ == "__main__":

    # Grab First and Second Argument

    image_folder = sys.argv[1]
    output_folder = sys.argv[2]

    # check is new/exists, if not create
    print(image_folder, output_folder)

    if not os.path.exists(output_folder):
        print("Path does not exists")
        os.makedirs(output_folder)
    else:
        print("Path Exists")

    # loop through Pokedex
    # convert images to png

    for filename in os.listdir(image_folder):
        img = Image.open(f"{image_folder}{filename}")
        # have to clean name - need to remove . jpg
        clean_name = os.path.splitext(filename)
        print(clean_name)
        img.save(f'{output_folder}{clean_name[0]}.png', 'png')
        print(f"Converted {filename}")
