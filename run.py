import bpy
from panel.panel import Panel

def register():
    bpy.utils.register_class(Panel)

def unregister():
    bpy.utils.unregister_class(Panel)

if __name__ == '__main__':
    register()