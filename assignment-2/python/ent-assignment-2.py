import maya.standalone
import maya.cmds as cmds
import argparse

maya.standalone.initialize()

parser = argparse.ArgumentParser(description='This program creates mini box-cars.')
parser.add_argument('num_cars', type=int, help='Number of cars')

args = parser.parse_args()

print("Creating {} box car(s)...".format(args.num_cars))

def car_creator():
    cmds.polyCube(d=7, h=5, w=5)
    wheel1 = cmds.polyCylinder(r=2, h=1, sa=10)
    cmds.select(wheel1)
    cmds.rotate(0, 0, 90)
    cmds.move(3, -2, 2.5)
    wheel2 = cmds.polyCylinder(r=2, h=1, sa=10)
    cmds.select(wheel2)
    cmds.rotate(0, 0, 90)
    cmds.move(-3, -2, -2.5)
    wheel3 = cmds.polyCylinder(r=2, h=1, sa=10)
    cmds.select(wheel3)
    cmds.rotate(0, 0, 90)
    cmds.move(3, -2, -2.5)
    wheel4 = cmds.polyCylinder(r=2, h=1, sa=10)
    cmds.select(wheel4)
    cmds.rotate(0, 0, 90)
    cmds.move(-3, -2, 2.5)

for i in range(args.num_cars):
    print("Created car #{}".format(i))
    car_creator()

print("Cars in the Maya scene: {}".format(args.num_cars))
print("Meshes in the Maya scene:")
print(cmds.ls(geometry=True))

cmds.file(rn='MiniCars')
cmds.file(s=True)
print("Saved!")




