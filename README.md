# souvenir

This project is for now a simple script to manipulate personal images.

## Context
When exporting image out of google photo, the filedate is set to the creation of the file, not the creation of the picture. Having the date of the picture set in the date of the file is convinent when organizing pictures locally.

## Overview
`update_image_dates.py` is a Python script that updates the file modification dates of images in a specified folder. It sets each image's file modification date to match the date found in the image's EXIF data. If EXIF data is not present or incomplete, the script can optionally use a default date provided by the user.

## Requirements
- Python 3
- Pillow library

## Installation
Before running the script, ensure that Python 3 is installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you need to install the Pillow library. You can install it using pip:

```bash
pip install Pillow
```

## Usage
To use update_image_dates.py, navigate to the script's location in your terminal and run it with the required folder path. You can also specify an optional default date.

### Basic usage:
```bash
python update_image_dates.py <folder_path>
```
Replace <folder_path> with the path to your folder containing the images.

### Example
```bash
python update_image_dates.py /path/to/images -d "2024-01-20 12:00:00" -a
```
This exemple shows how to set a default date to ALL files.
The default date should be in the format "YYYY-MM-DD HH:MM:SS".
Don't forget the "quotes".

It is recommended to back up your images before running this script, as it modifies file properties or incase something goes wrong.

## Parameters

### `folder`
- **Description**: Path to the folder containing files.
- **Required**: Yes
- **Usage**: `update_image_filedate.py <folder>`

### `-d`, `--default_date`
- **Description**: Default date in YYYY-MM-DD HH:MM:SS format. Applied to files if no EXIF date is found, or to all files when `-a`/`--all` is used.
- **Required**: No
- **Format**: `YYYY-MM-DD HH:MM:SS`
- **Usage**: `update_image_filedate.py <folder> -d "YYYY-MM-DD HH:MM:SS"`

### `-a`, `--all`
- **Description**: Apply the default date to all files within the specified folder, not just image files. Useful for setting a uniform date for a mix of file types.
- **Required**: No
- **Usage**: `update_image_filedate.py <folder> --all`


## License
Check the LICENSE file

## Disclaimer
This script is provided "as is", without warranty of any kind. Use it at your own risk.