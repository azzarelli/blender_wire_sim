import bpy
import sys

    
# set the PYDEV_SOURCE_DIR correctly before using the debugger
DIRSRC = "C:/Users/azzad/Documents/Blender Projects/virtual_studio/blender_wire_sim/"
# test if PYDEV_SOURCE_DIR already in sys.path, otherwise append it
if sys.path.count(DIRSRC) < 1:
    sys.path.append(DIRSRC)

import world as wrld
import imp
imp.reload(wrld)

if __name__ == "__main__":
    print('------ Test 1 ------')
    OBJS = list(bpy.data.objects)
    
    world = wrld.World(objects=OBJS)#
    
    # Define the height of this fl
    world.get_floor_height()
#    world.update_path_z_axis() # floor wire
#    world.populate_path(10)
    world.populate_path(15)
    print('zMin: ', world.z) 