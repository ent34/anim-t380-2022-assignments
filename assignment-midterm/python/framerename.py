# Script Name: Frame Configuration
# Author: Erika Taylor
# Date: October 22, 2022
'''
Description: This script collects an existing frame sequence, renames the frames, then
allows the user to zip the files if they so wish
'''

# Testing Script for running over process and ideas for process

import os
import argparse
from zipfile import ZipFile

# Creating a ZipFile
zipFolder = ZipFile('frame_sequence.zip', 'w')

# Set up arguments for user to enter naming convention
fileParser = argparse.ArgumentParser(description="This allows you to change specific parts of your file")
fileParser.add_argument("seqName", type=str, help="Name of frame sequence")
fileParser.add_argument("frameStart", type=int, help="Where you'd like your frame sequence to start")
fileParser.add_argument("fileType", type=str, help="Type of file")
fileParser.add_argument("zipFile", type=bool, help="To Zip or Not To Zip?")

args = fileParser.parse_args()

# Keeping number format together
if args.frameStart >= 100 and args.frameStart <= 999:
    frameInfo = {
        "front": "frame",
        "name": "{}".format(args.seqName),
        "number": "{}".format(args.frameStart),
        "ext": "{}".format(args.fileType)
    }
elif args.frameStart >= 10:
    frameInfo = {
        "front": "frame",
        "name": "{}".format(args.seqName),
        "number": "0{}".format(args.frameStart),
        "ext": "{}".format(args.fileType)
    }
else:
    frameInfo = {
        "front": "frame",
        "name": "{}".format(args.seqName),
        "number": "00{}".format(args.frameStart),
        "ext": "{}".format(args.fileType)
    }

# Establish file format
fileFormat = "{front}_{name}_{number}.{ext}"

'''
for originalFrame in folder:
    fileName = 'getFileName'
    fileRename = os.rename(fileName, fileFormat) # Add File Number Iteration somewhere
    if arg.zipFile == True:
        zipFolder.write('fileRename') # Adding each file to the zipped file???
    break

zipFolder.close() # Assuming that zipped file will save to that working directory

print(fileFormat.format(**frameInfo))

#getCwd = os.getcwd()
'''

