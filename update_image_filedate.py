# Update the file date of images to the EXIF date
from PIL import Image
import os
import datetime
import glob
import sys


def change_file_date_to_exif_date(file_path):
    try:
        with Image.open(file_path) as img:
            exif_data = img._getexif()
            if exif_data is not None:
                # 36867 is the tag for DateTimeOriginal
                date_time_original = exif_data.get(36867)
                if date_time_original:
                    new_date = datetime.datetime.strptime(
                        date_time_original, "%Y:%m:%d %H:%M:%S"
                    )
                    timestamp = new_date.timestamp()
                    os.utime(file_path, (timestamp, timestamp))
                    print(f"Date modified for '{file_path}' to {new_date}")
                else:
                    print(f"No original date found for '{file_path}'")
            else:
                print(f"No EXIF data found for '{file_path}'")
    except Exception as e:
        print(f"Error processing '{file_path}': {e}")


def process_folder(folder_path):
    for file_path in glob.glob(os.path.join(folder_path, "*.jpg")) + glob.glob(
        os.path.join(folder_path, "*.jpeg")
    ):
        change_file_date_to_exif_date(file_path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python update_image_dates.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    process_folder(folder_path)
