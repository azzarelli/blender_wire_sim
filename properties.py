import bpy
from bpy.types import PropertyGroup
from bpy.props import IntProperty, FloatProperty

class WireProperties(PropertyGroup):

    wire_num : IntProperty(
        name="Int Wire Num",
        description="Value for number of wires in a collection.",
        default = 1,
        min = 1, max = 10
    )

    arch_slack : FloatProperty(
        name="Arch Slack",
        description="Slack of the total wire.",
        default = .5,
        min = 0., max = 1.
    )

    wire_slack : FloatProperty(
        name="Segment Slack",
        description="Slack of segment (how loose is the wire).",
        default = .5,
        min = 0., max = 1.
    )