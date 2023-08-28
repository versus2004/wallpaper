#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import subprocess
import os
import random

def set_gnome_wallpaper(file_path):
    command = [
        "gsettings",
        "set",
        "org.gnome.desktop.background",
        "picture-uri",
        f"'file://{file_path}'"
    ]
    try:
        subprocess.run(command, check=True)
        print("Wallpaper changed with success.")
    except subprocess.CalledProcessError:
        print("An error occurred while setting a new wallpaper.")

if __name__ == '__main__':
    wallpaper_directory = "whole path of ur wallpaper"

    # Get a list of all files with jpg or jpeg extension
    image_files = [f for f in os.listdir(wallpaper_directory) if f.lower().endswith((".jpg", ".jpeg"))]

    if image_files:
        # Select a random image file from the list
        random_image = random.choice(image_files)
        image_path = os.path.join(wallpaper_directory, random_image)

        set_gnome_wallpaper(image_path)
    else:
        print("No image files found in the directory.")
