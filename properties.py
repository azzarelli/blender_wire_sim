import bpy
from bpy.types import PropertyGroup
from bpy.props import IntProperty

class WireProperties(PropertyGroup):

    wire_num : IntProperty(
        name="Int Wire Num",
        description="Value for number of wires in a collection.",
        default = 1,
        min = 1, max = 10
    )