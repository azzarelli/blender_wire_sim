import bpy
import imp

from classes import wire as wire_lib
import variables
imp.reload(variables)
imp.reload(wire_lib)

VARS = variables.vars

class GenWireOperator(bpy.types.Operator):
    bl_idname = 'opr.gen_wire_operator'
    bl_label = 'WireGen'

    def execute(self, context):
        scene = context.scene

       

        msg = VARS.wire.init_generation(scene.objects)
        print(msg)

        return {'FINISHED'}

class DelWireObjectOperator(bpy.types.Operator):
    bl_idname = 'opr.del_wire_operator'
    bl_label = 'WireGen'

    def execute(self, context):
        scene = context.scene
        msg = VARS.wire.delete_object(scene.objects)

        return {'FINISHED'}

class LoadResultOperator(bpy.types.Operator):
    bl_idname = 'opr.load_result_operator'
    bl_label = 'WireGen'

    def execute(self, context):
        scene = context.scene

        props = scene.wire_tool
        msg = VARS.wire.load_result(props, scene)

        print(msg)


        return {'FINISHED'}