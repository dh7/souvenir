# souvenir

This project is for now a simple script to manipulate personal images.

## Context
When exporting image out of google photo, the filedate is set to the creation of the file, not the creation of the picture. Having the date of the picture set in the date of the file is convinent when organizing pictures locally.

## Update_image_filedate.py
This script loads the exif data and write the date as the creation date of the file.

## Usage
```bash
Python update_image_filedate folder_name
```