import bpy
import bmesh
import math
import random

class Wire:
    def define_nodes(self, verts):
        verts_ = list(verts)
        N = len(verts_)

        self.x1 = verts[0]
        self.xN = verts[N-1]
        self.xArch = [v for idx,v in enumerate(verts) if ((idx != 0) and (idx != N-1))]

        self.verts = []
        for v in verts:
            v0 = self.mw @ v.co
            self.verts.append([v0.x, v0.y])

        self.nverts = len(self.verts)

    def init_edge_map(self, edges):
        edges = list(self.data.edges)
        for e in edges:
            verts = list(e.vertices)
            self.edge_map[f'{verts[0]}_{verts[1]}'] = {"fixed":{f'{verts[0]}':'', f'{verts[1]}':''}, "var":{}}


    def __init__(self, obj) -> None:
        self.obj = obj
        self.data = obj.data
        self.mw = obj.matrix_world
        
        self.edge_map = {}
        self.define_nodes(self.data.vertices)
        self.init_edge_map(self.data.edges)

    def edge_map_update(self):
        """Update EdgeMap 
        """
        keys = self.edge_map.keys()
        for idx, p in enumerate(self.data.vertices): # for each vertex
            p_ = self.mw @ p.co

            if [p_.x, p_.y] not in self.verts: # if point not previously registered
                for k in keys:
                    s = k.split('_')
                    
                    v0 = self.mw @ self.data.vertices[int(s[0])].co
                    v1 = self.mw @ self.data.vertices[int(s[1])].co

                    xA, yA = v0.x, v0.y
                    xB, yB = v1.x, v1.y

                    
                    if xA <= xB:
                        xmin = xA
                        xmax = xB
                    else:
                        xmin = xB
                        xmax = xA
                    if yA <= yB:
                        ymin = yA
                        ymax = yB
                    else:
                        ymin = yB
                        ymax = yA
                    
                    if (p_.x >= xmin) and (p_.x <= xmax) and (p_.y >= ymin) and (p_.y <= ymax):
                        self.edge_map[k]['var'][f'{idx}'] = ''
       

        print(self.edge_map)

    def update_pos(self):
        keys = self.edge_map.keys()

        for key in keys:
            K = list(self.edge_map[key]['var'].keys())
            for k in K:
                newpos = self.edge_map[key]['var'][k] # get new position of vertex from edge map
                v = self.data.vertices[int(k)] # get vertex object
                
                pos_world = self.mw @ v.co
                pos_world.x = newpos[0]
                pos_world.y = newpos[1]
                v.co = self.mw.inverted() @ pos_world
                

                # if [p.co.x, p.co.y] not in self.verts:
                # if i < cuts-1:
                #     print(f' {cnt}  {i}')
                #     pos_world = self.mw @ p.co
                #     pos_world.x = coords[cnt][0][i]
                #     pos_world.y = coords[cnt][1][i]
                #     p.co = self.mw.inverted() @ pos_world
                
                #     i += 1

                # else:
                #     cnt += 1
                #     i = 0



    def uniform_transform(self, cuts):
        
        keys = self.edge_map.keys()

        for key in keys:
            s = key.split('_')
            K = list(self.edge_map[key]['var'].keys())
            # TODO - order keys

            pos0 = self.mw @ self.data.vertices[int(s[0])].co
            pos1 = self.mw @ self.data.vertices[int(s[1])].co
            xA = [pos0.x, pos0.y]
            xB = [pos1.x, pos1.y]

            for k in K:
                print(k)
                t = self.mw @ self.data.vertices[int(k)].co
                
                print(f'{t}, {xA}, {xB}')
                self.edge_map[key]['var'][k] = self.f_transform(t, xA, xB)

        self.update_pos()


    def f_transform(self, t, xA, xB):
        
        if (xB[0] - xA[0]) == 0:
            m = float(xB[1] - xA[1])
        else:
            m = float(xB[1] - xA[1])/float(xB[0] - xA[0])
        
        th = math.atan(m)
        c = math.cos(th)
        s = math.sin(th)
        A = .02
        K = (xB[0]-xA[0])/c


        # X = K*((c * t.x) - (s * math.sin(2*math.pi*t.x))) + xA[0]
        
        # Y = K*((s * t.y)+ (A * c * math.sin(2* math.pi * t.y))) + xA[1]

        X = t.x + random.random()/10
        Y = t.y + random.random()/10
        return [X, Y]
        







