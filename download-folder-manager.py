# This script move files from download folder
# based on the filetype to the proper destination folder.

import os
import shutil
import pathlib

# todo automatically recognize username
# todo destination should be a folder in date-format to find easier.

dl_directory = "/home/dkurnosenko/Downloads"
stl_directory = "/home/dkurnosenko/Dokumente/3D-Prints/Models"
gcode_directory = "/home/dkurnosenko/Dokumente/3D-Prints/Printfiles"
video_directory = "/home/dkurnosenko/Video"

pathlib.Path(stl_directory).mkdir(parents=True, exist_ok=True)
pathlib.Path(gcode_directory).mkdir(parents=True, exist_ok=True)
pathlib.Path(video_directory).mkdir(parents=True, exist_ok=True)

for filename in os.listdir(dl_directory):
    if filename.endswith(".stl"):
        source = os.path.join(dl_directory, filename)
        destination = os.path.join(stl_directory, filename)
        dest = shutil.move(source, destination)

    if filename.endswith(".gcode"):
        source = os.path.join(dl_directory, filename)
        destination = os.path.join(gcode_directory, filename)
        dest = shutil.move(source, destination)

    if filename.endswith(".mov") or filename.endswith(".mp4"):
        source = os.path.join(dl_directory, filename)
        destination = os.path.join(video_directory, filename)
        dest = shutil.move(source, destination)