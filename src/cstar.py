class Cstar:
    def __init__(self, map_config):
        self.map_config = map_config
        self.length_weight = 0.7
        self.t_add_weight = 0.3
        self.START_POINT = [0, 1, 2, 3]
        self.CLOSED_POINT = [29, 49]

    # 返回以某一点为起点的最长路径
    def cal_longest_route(self, start_node):
        self.best_route = None

        visited = [False] * len(self.map_config.keys())
        path = []
        self.__all_route(start_node, 15, visited, path)

        # for i in range(10):
        #     visited = [False] * len(self.map_config.keys())
        #     path = []
        #     self.__all_route(start_node, i, visited, path)

        # for node in self.map_config.keys():
        #     visited = [False] * len(self.map_config.keys())
        #     path = []
        #     self.__all_route(start_node, node, visited, path)

        return self.best_route

    # 计算某一条路线的权值，权值越大路线越佳
    def get_route_weight(self, route):
        length = len(route)
        
        t_add = 0
        for i in range(length):
            if i - 1 not in route:
                t_add += 1
            else:
                last_link_num = len(self.map_config[route[i - 1]]['link_nodes'])
                if last_link_num > 1:
                    last_link_num -= 1
                t_add += 1 / last_link_num
                # t_add += 1

        return self.length_weight * length + self.t_add_weight * t_add, length, t_add

    # 处理递归算法pop出的一条路线
    def __pop_route(self, route):
        if not self.__check_route_valid(route):
            return

        if not self.best_route:
            self.best_route = route
            self.best_weight = self.get_route_weight(self.best_route)
        else:
            route_weight = self.get_route_weight(route)
            if route_weight > self.best_weight:
                self.best_route = route

    num = 0
    
    # 递归算法
    def __all_route(self, s, e, visited, path):
        visited[s] = True
        path.append(s)

        if s == e:
            self.__pop_route(path[:])
        else:
            node_config = self.map_config[s]
            for link_node in node_config['link_nodes']:
                if link_node not in self.START_POINT and link_node not in self.CLOSED_POINT and visited[link_node] == False:
                    self.num += 1
                    self.__all_route(link_node, e, visited, path)

        path.pop()
        visited[s] = False

    # 判断某条路线是否合法，必须满足以下条件
    # 1. 路线中的点唯一，不允许出现重复的点（递归算法本身不会产出这种路线）
    # 2. 路线中的所有点只能两两相连，不允许出现多点相连的情况 
    def __check_route_valid(self, route):
        valid = True
        last_node = -1

        closed_nodes = []
        route_length = len(route)

        for i in range(route_length):
            pass_node = route[i]
            if pass_node in closed_nodes:
                valid = False
                break

            closed_nodes.append(pass_node)
            if last_node >= 0:
                for link_node in self.map_config[last_node]['link_nodes']:
                    if link_node not in closed_nodes:
                        closed_nodes.append(link_node)

            last_node = pass_node

        return valid
