import bpy
# import sys

    
# # set the PYDEV_SOURCE_DIR correctly before using the debugger
# DIRSRC = "C:/Users/azzad/Documents/Blender Projects/virtual_studio/"
# # test if PYDEV_SOURCE_DIR already in sys.path, otherwise append it
# if sys.path.count(DIRSRC) < 1:
#     sys.path.append(DIRSRC)

# import pydevd module
import world as wrld

def run():
    OBJS = list(bpy.data.objects)
    
    world = wrld.World(objects=OBJS)#
    
    # Define the height of this fl
    world.get_floor_height()
    
    print('zMin: ', world.z) 