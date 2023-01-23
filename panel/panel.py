import bpy

class Panel(bpy.types.Panel):
    bl_idname = 'VIEW3D_PT_Wire_Gen_Pan'
    bl_label = 'WireGen'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    

    def draw(self, context):
        wire_tool = context.scene.wire_tool
        
        col = self.layout.column()

        col.operator('opr.gen_wire_operator', text='Generate Arch Map')
        col.operator('opr.del_wire_operator', text='Delete Cable')


        col.prop(wire_tool, "wire_num")

        
