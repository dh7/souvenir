# Update the file date of images to the EXIF date
# If no EXIF date is available, use the default date
# If no default date is provided, the file date is not changed
#
# Usage: update_image_filedate.py <directory>
#        update_image_filedate.py <directory> -d "2020-01-01 12:00:00"

import argparse
import datetime
import glob
import os
from PIL import Image, UnidentifiedImageError


def change_file_date(file_path, default_date=None, is_image=True):
    try:
        new_date = None
        if is_image:
            with Image.open(file_path) as img:
                exif_data = img._getexif()
                if exif_data:
                    date_time_original = exif_data.get(
                        36867
                    )  # 36867 is the tag for DateTimeOriginal
                    if date_time_original:
                        new_date = datetime.datetime.strptime(
                            date_time_original, "%Y:%m:%d %H:%M:%S"
                        )

        if new_date is None and default_date:
            new_date = default_date

        if new_date:
            timestamp = new_date.timestamp()
            os.utime(file_path, (timestamp, timestamp))
            print(f"Date modified for '{file_path}' to {new_date}")
        else:
            print(f"No valid date for '{file_path}'. Skipping.")
    except UnidentifiedImageError:
        if default_date and not is_image:
            change_file_date(file_path, default_date, is_image=False)
    except Exception as e:
        print(f"Error processing '{file_path}': {e}")


def process_folder(folder_path, default_date=None, set_default_for_all=False):
    for file_path in glob.glob(os.path.join(folder_path, "*")):
        if file_path.lower().endswith((".jpg", ".jpeg")):
            change_file_date(file_path, default_date, is_image=True)
        elif set_default_for_all:
            change_file_date(file_path, default_date, is_image=False)


def parse_date(date_string):
    try:
        return datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        raise argparse.ArgumentTypeError("Date must be in YYYY-MM-DD HH:MM:SS format")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Update file dates based on EXIF data or a default date."
    )
    parser.add_argument("folder", help="Path to the folder containing files")
    parser.add_argument(
        "-d",
        "--default_date",
        help="Default date in YYYY-MM-DD HH:MM:SS format",
        type=parse_date,
    )
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="Apply default date to all files, not just images",
    )
    args = parser.parse_args()

    process_folder(args.folder, args.default_date, args.all)
