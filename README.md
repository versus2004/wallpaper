
# Wallhaven Wallpaper Downloader

![GitHub](https://img.shields.io/github/license/yversus2004/wallpaper)
![Python](https://img.shields.io/badge/python-3.6%2B-blue)
![Dependencies](https://img.shields.io/badge/dependencies-requests-brightgreen)

A simple Python script to search for and download wallpapers from Wallhaven.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Overview
This script allows you to search for wallpapers on Wallhaven and download them to a specified directory. It utilizes the Wallhaven API to fetch wallpaper details and download links.

## Features
- Search and download wallpapers from Wallhaven
- Automatically generates unique filenames for downloaded wallpapers

## Prerequisites
- Python 3.6 or higher
- [requests](https://pypi.org/project/requests/) Python library

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/versus2004/wallpaper.git
   ```

2. Change to the project directory:
   ```sh
   cd wallpaper
   ```

3. Install the required Python libraries:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the script with a search query to download wallpapers based on that query. Replace `<search_query>` with your desired query:
```sh
python waldl.py <search_query>
```

For example, to download anime wallpapers, you can run:
```sh
python waldl.py anime wallpapers
```
