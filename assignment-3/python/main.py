# Script Name: Assignment 3
# Author: Erika Taylor
# Date: October 11, 2022
# This script creates an empty group in maya with the alias asset name and saves it

import os
import sys
import maya.cmds as mc
import maya.standalone

# Runs maya
maya.standalone.initialize()

# Establishes environment variable
asset = os.getenv('asset')

# Creates empty group with asset name
mc.group(em=True, n=asset)

# Changing to D: directory
os.chdir('D:\\ANIMT380\\anim-t380-2022-assignments\\assignment-3')

getCwd = os.getcwd()

# Path to created directory
dirPath = 'assets\\{asset}\\maya\\scenes\\emptygroupizzy.mb'.format(asset=asset)

# Joining the full save path together
fullPath = os.path.join(getCwd, dirPath)

# Saves file to path as mb
mc.file(rn=(fullPath))
mc.file(save=True)




