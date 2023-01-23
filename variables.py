import bpy
import imp

from classes import wire as wire_lib

imp.reload(wire_lib)

class Vars():
    wire = wire_lib.Wire()

vars = Vars()