"""Class Definition for the 'World' environment.#
        - Puposed for determining 'natural' (and configurable) placement of cables in a scene.
        - Also includes checking inputs
"""
import bpy
import bmesh
from mathutils import Vector, Matrix



def validate(flag:str='', params:tuple=(0, 'NA')):
    val = 0
    if params != (0, "NA"):
        # Validate Inputs for initialisation of class
        if flag == "initialisation":
            co, arch = params
            if len(co) != 2: # coords must be a list of two
                val = 1
                print(f"Error : Input Coordinates for World should only contain start and end coordinates.")
            else:
                if (len(co[0]) != 2) or (len(co[1]) != 2): # each coord must be 2D
                    val = 1
                    print(f"Error : Coordinates should be 2D (along x and y axis).")
                elif (type(co[0][0]) != type(.1)) or (type(co[1][0]) != type(.1)):
                    val = 1
                    print(f"Error : Start/End cordinates are not of type float.")
                else:
                    if len(arch) > 0: # if arch coords exist we need to validate them
                        for p in arch:
                            if len(p) != 2: # if arch coords are lenth 2
                                val = 1
                                print(f"Error : Arch Param {p} is not 2D (along x and y axis).")
                            elif type(p[0]) != type(0.1): # check if list is a float list
                                val = 1
                                print(f"Error : Arch Param {p} must be float types.")


class World():
    def load_scene_as_world(self, OBJS):
        """Loading in Scene parameters to match World simulation
        """

        # Extract desired data from NAME specific objects
        for o in OBJS:
            if o.name == "room":
                self.room = o
                self.room_data = o.data
                self.r_faces = list(self.room_data.polygons)

            if o.name == "wire_path":
                print('Wire')
                self.wire = bpy.data.objects["wire_path"]
                self.w_mat_world = self.wire.matrix_world


    def __init__(self, coords:list=[[.0,.0], [.1, .1]], arches:list=[], objects:list=[]):
        """Initialising World object

        Inputs:
            coords : List of List
                Should contain a list of 2 sets of coordinates, for start and end coordinates (2D x,y axis)
            arches : List of List
                Should contain a list of 2D coordinates which identify a position of 'major bend' in a cable system 
        """
        validate(flag="initialisation", params=(coords, arches))

        self.z = 0

        self.verts = []
        self.edges = []
        self.polygons = []

        self.room = ''
        self.wire = ''
        self.room_data = []
        self.r_faces = []
        self.p_verts = []

        if objects != []:
            self.load_scene_as_world(objects)
            print(self.wire)
    
    def update_path_z_axis(self):
        """Update the z-axis of the given path object
        
        Inputs:
            OBJS : List of bpy.data.objects
                Contains a list of objects in our scene - from which we extract one labelled 'wire path'

        """
        if self.wire != '':
            for p in self.wire.data.vertices:
                pos_world = self.w_mat_world @ p.co
                pos_world.z = self.z
                p.co = self.w_mat_world.inverted() @ pos_world


    def populate_path(self, target:int=0):
        if target > 0:
            n_verts = len(self.wire.data.vertices) -2 # get number of edges
            n_edges = n_verts + 1
            mul = int((target-n_verts)/n_edges )

            if mul > 1:
                bm = bmesh.new()
                me = self.wire.data
                bm.from_mesh(me)

                bmesh.ops.subdivide_edges(bm,
                edges=bm.edges, 
                cuts=mul, 
                use_grid_fill=True,    
                )

                bm.to_mesh(me)
                me.update()
            else:
                print('Error : Population scaling is less than 1')

    def f_linear_combination(self, coords:list=[]):
        

    def get_floor_height(self):
        """Determines the floor height for placing wires on floor
        Input:
            OBJS : List of bpy.data.objects
                Contains a list of objects in our scene - from which we extract one labelled 'room' (a Mesh object)

        Notes : 
                Currently only possible if wall polygons are < floor and ceiling Polygons. Floor needs to be uniform. 'room' needs to be a planar-cube mesh (i.e. non-volumetric surfaces)
        """
        # If room object exists
        if self.room != '':
            min = 100000

            # Take the polygon(s) with the largest areas 
            #     (Making the assumption that the floor/ceiling areas are larger than the walls)
            max = 0
            fmax = []
            for f in self.r_faces:
                if f.area > max:
                    max = f.area

            for f in self.r_faces:
                if f.area == max:
                    fmax.append(f)
            
            # Get the height of the flat floor (lowest polygon)
            min = 10000
            for f in fmax:
                fverts = list(f.vertices)
                if self.room_data.vertices[fverts[0]].co.z < min:
                    min = self.room_data.vertices[fverts[0]].co.z
            
            self.z = min
            print(min, ' ', self.z)
        else:
            print('Error : No object called `room` defined.')
            
