# Script Name: Version Save
# Author: Erika Taylor
# Date: October 16, 2022
# Description: This script takes the current file naming convention and saves it as the next version of that file

import os
import maya.cmds as mc
import maya.standalone

maya.standalone.initialize()

# Establish base file name variable
fileName = "vincent.rig.etaylor.1"

# Rename File
mc.file(rn=fileName)

# Save File
mc.file(s=True, typ="mayaAscii")

# Split File and Increment Number
fileSplit = str(mc.file(sn=True)).split(".")
fileSplit[3] = str(int(fileSplit[3]) + 1)

# Rename File
fileName = fileSplit.join(".")
mc.file(rn=fileName)

# Save File
mc.file(s=True)






