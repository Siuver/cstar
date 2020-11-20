class Cstar:
    def __init__(self, map_config):
        self.map_config = map_config
        self.length_weight = 0.7
        self.t_add_weight = 0.3

    # 返回以某一点为起点的最长路径
    def cal_longest_route(self, start_node):
        self.best_route = None

        for node in self.map_config.keys():
            visited = [False] * len(self.map_config.keys())
            path = []
            self.__all_route(start_node, node, visited, path)

        return self.best_route

    # 计算某一条路线的权值，权值越大路线越佳
    def get_route_weight(self, route):
        length = len(route)
        
        t_add = 0
        for i in range(length):
            if i - 1 not in self.map_config:
                t_add += 1
            else:
                t_add += 1 / (len(self.map_config[i - 1]['link_nodes']) - 1)

        return self.length_weight * length + self.t_add_weight * t_add, length, t_add

    # 处理递归算法pop出的一条路线
    def __pop_route(self, route):
        if not self.__check_route_valid(route):
            return

        if not self.best_route:
            self.best_route = route
        else:
            cur_best_weight = self.get_route_weight(self.best_route)
            route_weight = self.get_route_weight(route)
            if route_weight > cur_best_weight:
                self.best_route = route

    # 递归算法
    def __all_route(self, s, e, visited, path):
        visited[s] = True
        path.append(s)

        if s == e:
            self.__pop_route(path[:])
        else:
            node_config = self.map_config[s]
            for link_node in node_config['link_nodes']:
                if visited[link_node] == False:
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
