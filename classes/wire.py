import math

class Wire:
    def __init__(self, obj) -> None:
        self.vert_map = {"end":{ "0":[0,0,0], "1":[0,1,0]},
                        "arch":{}}
        self.edge_map = {"fixed":{"0_1":["", ""]}}

    

    def update_ends(self, a, b):
        self.vert_map["end"]["0"] = a
        self.vert_map["end"]["1"] = b






