import tkinter as tk
from cstar import Cstar

MAP_SIZE = 1024
COMMON_SCALE = 0.8

class MyTk:
    def __init__(self, map_config):
        self.map_config = map_config
        self.cstar = Cstar(self.map_config)

        self.__init_node_dict()
        self.__init_tk()
        self.__init_map()

        self.window.mainloop()

    def __init_tk(self):
        self.window = tk.Tk()
        self.window.title("路线")
        size = MAP_SIZE * COMMON_SCALE
        self.window.geometry("%dx%d" % (size, size))

        self.canvas = tk.Canvas(self.window, width=size, height=size)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.__ontouch)

        # self.window.mainloop()

    def __init_map(self):
        for key, value in self.map_config.items():
            for link_node in value["link_nodes"]:
                self.line(key, link_node)

        for key, value in self.map_config.items():
            self.dot(key)

    def __init_node_dict(self):
        self.node_dict = {}
        for key, value in self.map_config.items():
            self.node_dict[key] = {"dot": None, "path": {}}

    def __ontouch(self, e):
        best_route = self.cstar.cal_longest_route(0)
        self.mark_route(best_route)
        pass

    def dot(self, node, fill="white", **kw):
        id = None

        if self.node_dict[node]["dot"] is not None:
            id = self.node_dict[node]["dot"]

        if id is None:
            nodecfg = self.map_config[node]
            radius = 5
            x = nodecfg["x"] * COMMON_SCALE
            y = nodecfg["y"] * COMMON_SCALE
            id = self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=fill, **kw)
            self.node_dict[node]["dot"] = id
        else:
            self.canvas.itemconfig(id, fill=fill, **kw)

        return id

    def line(self, node1, node2, fill="black", **kw):
        id = None

        if node2 in self.node_dict[node1]["path"]:
            id = self.node_dict[node1]["path"][node2]

        if id is None:
            cfg1 = self.map_config[node1]
            cfg2 = self.map_config[node2]
            id = self.canvas.create_line(cfg1["x"] * COMMON_SCALE, cfg1["y"] * COMMON_SCALE, cfg2["x"] * COMMON_SCALE, cfg2["y"] * COMMON_SCALE, fill=fill, **kw)
            self.node_dict[node1]["path"][node2] = id
            self.node_dict[node2]["path"][node1] = id
        else:
            self.canvas.itemconfig(id, fill=fill, **kw)

        return id

    def mark_route(self, route):
        length = len(route)
        for i in range(length):
            if i == length - 1:
                break

            self.line(route[i], route[i + 1], "red")
