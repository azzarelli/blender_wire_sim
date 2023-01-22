import bpy
import bmesh

class Wire:
    def define_nodes(self, verts):
        verts_ = list(verts)
        N = len(verts_)
        print(f'N {N}')

        self.x1 = verts[0]
        self.xN = verts[N-1]
        self.xArch = [v for idx,v in enumerate(verts) if ((idx != 0) and (idx != N-1))]



    def __init__(self, obj) -> None:
        self.obj = obj
        self.data = obj.data
        self.mw = obj.matrix_world

        self.define_nodes(self.data.vertices)

