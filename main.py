import sys
import os
from PIL import Image

"""
Use the terminal

python main.py Pokedex\ new\
"""
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# print(image_folder, output_folder)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')


