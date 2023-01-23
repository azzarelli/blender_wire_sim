bl_info = {
    "name": "Wire Gen Add-on",
    "description": "",
    "author": "Adrian Azzarelli",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "3D View > Tools",
    "warning": "", # used for warning icon and text in addons panel
    "wiki_url": "",
    "tracker_url": "",
    "category": "Development"
}


import bpy
import sys
import imp


DIRSRC = "C:/Users/azzad/Documents/Blender Projects/virtual_studio/blender_wire_sim/"
# test if PYDEV_SOURCE_DIR already in sys.path, otherwise append it
if sys.path.count(DIRSRC) < 1:
    sys.path.append(DIRSRC)
    
import world
imp.reload(world)

if __name__ == '__main__':
    WORLD = world.World(unreg=0)