import bpy

class Panel(bpy.types.Panel):
    bl_idname = 'Wire_Gen_Pan'
    bl_label = 'WireGen'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        self.layout.label(text='Hello world')