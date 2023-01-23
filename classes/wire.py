import bpy
import math

class Wire:
    name = "wire_object"

    verts = [(0,0,0),(1,0,0)]
    edges = [(0,1)]
    faces = []  

    def __init__(self) -> None:
        self.vert_map = {"edge":{ "0":self.verts[0], "1":self.verts[1]},
                        "arch":{}}
        self.edge_map = {"fixed":{f"{self.edges[0][0]}_{self.edges[0][1]}":["", ""]}}


    def init_generation(self, OBJS) -> str:
        """Generate an initial wire-frame at the center of the world
        """
        # Check if mesh already exists
        for o in OBJS:
            if o.name == self.name:
                return 'Object-mesh already Exists'

        # If not then create mesh and associate with object
        mesh = bpy.data.meshes.new('wire_mesh')
        mesh.from_pydata(self.verts, self.edges, self.faces)

        obj = bpy.data.objects.new('wire_object', mesh)
        bpy.context.collection.objects.link(obj)

        return f'Object-mesh {self.name} created'


    def delete_object(self, OBJS) -> str:
        """Delete the wire-frame object
        """
        for o in OBJS:
            if o.name == self.name:
                bpy.data.objects.remove(OBJS[self.name], do_unlink=True)
                return f'Deleted Object : {self.name}'
        return f'No Object Deleted (Doesn t exist)'


    def load_result(self, props, scene):
        """Update the new placement of our mesh and Generate a new cable
        """
        # Determine if object exists
        found = 0
        for o in scene.objects:
            if o.name == self.name:
                found = 1
        
        if found == 0:
            return f'No Object Found'

        # Get the vertices and edges of the new mesh

        return f'Nothing Loaded ya dumbass'






