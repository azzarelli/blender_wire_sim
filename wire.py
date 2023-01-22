import bpy
import bmesh
import math

class Wire:
    def define_nodes(self, verts):
        verts_ = list(verts)
        N = len(verts_)

        self.x1 = verts[0]
        self.xN = verts[N-1]
        self.xArch = [v for idx,v in enumerate(verts) if ((idx != 0) and (idx != N-1))]
        self.verts = [[v.co.x, v.co.y] for v in verts]



    def __init__(self, obj) -> None:
        self.obj = obj
        self.data = obj.data
        self.mw = obj.matrix_world

        self.define_nodes(self.data.vertices)
    
    def update_transform_pos(self, coords, cuts):
        
        cnt = 0
        i = 0
        for idx, p in enumerate(self.data.vertices):
            if [p.co.x, p.co.y] not in self.verts:
                print(p.co)
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
            else:
                print(p.co)


    def uniform_transform(self, cuts):
        verts = list(self.data.vertices)
        
        new_cut_pos = []

        for i in range(len(verts) -1):
            pos = self.mw @ verts[i].co
            pos_1 = self.mw @ verts[i+1].co
            xA, xB = [pos.x, pos.y], [pos_1.x, pos_1.y]

            x, y = self.f_transform(xA, xB, cuts)
            new_cut_pos.append([x,y])
        self.update_transform_pos(new_cut_pos, cuts)

    def f_transform(self, xA, xB, steps):
        
        if (xB[0] - xA[0]) == 0:
            m = float(xB[1] - xA[1])
        else:
            m = float(xB[1] - xA[1])/float(xB[0] - xA[0])
        
        th = math.atan(m)
        c = math.cos(th)
        s = math.sin(th)
        A = -m/(2*math.pi)
        K = (xB[0]-xA[0])/c

        x, y = [], []
        T = [float(i)/float(steps) for i in range(steps+1)]
        for t in T:
            X = K*((c * t) - (s * math.sin(2*math.pi*t))) + xA[0]
            x.append(X)
            Y = K*((s * t)+ (A * c * math.sin(2* math.pi * t))) + xA[1]
            y.append(Y)
        return x[1:len(x)-1], y[1:len(y)-1]
        







