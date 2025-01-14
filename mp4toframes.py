# -*- coding: utf-8 -*-
"""mp4toFrames

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1imO3h-36Xf9S-hsxZk0Y4RSrG0BRfOcr
"""

import cv2
import random

every_n_frame = 60
grayscale = False
rotations = False
resized = False

vidcap = cv2.VideoCapture('test2.mp4')
success, image = vidcap.read()
count = 0
x = 640
y = 640

while success:
  if count % every_n_frame == 0:
    if grayscale:
      image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if rotations:
      rotation = random.randint(1,4)
      if rotation == 1:
        image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
      elif rotation == 2:
        image = cv2.rotate(image, cv2.ROTATE_180)
      elif rotation == 3:
        image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    if resized:
      image = cv2.resize(image, (x, y))
    cv2.imwrite(f"frame{count}.jpg", image)  # Saves the frame as a JPEG file
    print(f"Captured frame {count}")
  success, image = vidcap.read()
  count += 1

import zipfile
import os

def zip_jpg_files(folder_path, zip_name):
    # Create a zip file
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        # Iterate through all files in the folder
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.jpg'):  # Only add JPG files
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, arcname=file)  # Add file to zip

    print(f'All .jpg files in "{folder_path}" have been zipped into "{zip_name}".')

# Usage
folder_path = '/content'  # Replace with your folder path
zip_name = 'images.zip'  # Name of the zip file
zip_jpg_files(folder_path, zip_name)