# Script Name: Frame Configuration
# Author: Erika Taylor
# Date: October 22, 2022
'''
Description: This script collects an existing frame sequence, renames the frames based on the json naming convention,
then allows the user to zip the files if they so wish
'''

# Testing Script for running over process and ideas for process

import os
import argparse
import json
import shutil as zip

# Set up arguments for user to enter path and choice of zipping
fileParser = argparse.ArgumentParser(description="This allows you to specify frame location and zip the file")
fileParser.add_argument("seqLocation", type=str, help="Location path of frame sequence")
fileParser.add_argument("zipFile", type=bool, help="To Zip or Not To Zip?")

arg = fileParser.parse_args()

# Get naming convention
getNamingConvention = open("sequenceConvention.json")
namingConvention = json.load(getNamingConvention)

# Establish file name format
fileFormat = "{sequence}.{task}.{artist}.{version}.{frame}.{ext}".format(**namingConvention)

def frameInc(file):
    sF = file.split(".")
    sF[4] = str(int(sF[4]) + 1).zfill(4)
    newFile = ".".join(sF)
    return newFile

# Increment file
for i in os.listdir(arg.seqLocation):
    os.rename(arg.seqLocation + "/" + i, arg.seqLocation + "/" + fileFormat)
    print("New Name: ", fileFormat)
    fileFormat = frameInc(fileFormat)

# Creating a ZipFile in Current Working Directory
if arg.zipFile == True:
    zipFile = zip.make_archive("renamed_frame", "zip", arg.seqLocation)

# Variable for current working directory
getCwd = os.getcwd()

# Change zip file location from current directory to frame sequence location
zipLocation = zip.move(os.path.join(getCwd, zipFile), arg.seqLocation)

# Print current zip file location
print("Destination of Zip File:", zipLocation)



