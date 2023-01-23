import bpy
import imp
from bpy.props import PointerProperty

from panel import panel, operator
import properties

imp.reload(panel)
imp.reload(operator)
imp.reload(properties)

class World:
    props = {"Int Wire Num":properties.WireProperties}
    oprs = {'opr.gen_wire_operator':operator.GenWireOperator, 'opr.del_wire_operator':operator.DelWireObjectOperator}
    cls = {"VIEW3D_PT_Wire_Gen_Pan":panel.Panel}

    def register(self, o, c):
        if o == "Int Wire Num":
            bpy.utils.register_class(c)

            bpy.types.Scene.wire_tool = PointerProperty(type=properties.WireProperties)
        else:
            bpy.utils.register_class(c)
    

    def unregister(self, o, c):
        if o == "Int Wire Num":
            bpy.utils.unregister_class(c)
            del bpy.types.Scene.wire_tool
        else:
            bpy.utils.unregister_class(c)
        

        return 200

    def load(self, f:int=0):
        pk = self.props.keys()
        ok = self.oprs.keys()
        ck = self.cls.keys()


        for p in pk:
            if (hasattr(bpy.types, p) and f==3) or f == 1:
                print(f'Prop {p}')
                self.unregister(p, self.props[p])
            else:
                self.register(p, self.props[p])
            
        for p in ok:
            if (hasattr(bpy.types, p) and f==3) or f ==1:
                print(f'Opr {p}')
                self.unregister(p, self.oprs[p])
            else:
                self.register(p, self.oprs[p])

        for p in ck:
            if (hasattr(bpy.types, p) and f==3) or f ==1:
                print(f'Pan {p}')
                self.unregister(p, self.cls[p])
            else:
                self.register(p, self.cls[p])
    
    def __init__(self, unreg:int=0) -> None:
        self.load(f=unreg)

        