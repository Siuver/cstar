import map


class Cstar:
    def __init__(self, mapConfig):
        self.mapConfig = mapConfig

    def all_route(self, s, e, visited, path, node2route):
        visited[s] = True
        path.append(s)

        if s == e:
            if e not in node2route:
                node2route[e] = []
            node2route[e].append(path[:])
        else:
            nodeConfig = self.mapConfig[s]
            for linkNode in nodeConfig['link_node']:
                if visited[linkNode] == False and nodeConfig['valid'] == True:
                    self.all_route(linkNode, e, visited, path, node2route)

        path.pop()
        visited[s] = False

    def checkRouteValid(self, route):
        valid = True
        lastNode = -1

        closedNode = []
        routeLength = len(route)

        for i in range(routeLength):
            passNode = route[i]
            if passNode in closedNode:
                valid = False
                break

            closedNode.append(valid)
            if lastNode >= 0:
                for linkNode in self.mapConfig[lastNode]['link_node']:
                    if linkNode not in closedNode:
                        closedNode.append(linkNode)

            lastNode = passNode

        return valid

    def cal_longest_route(self, startNode):
        longest_route = []

        node2route = {}
        for node in self.mapConfig.keys():
            visited = [False] * len(self.mapConfig.keys())
            path = []
            self.all_route(startNode, node, visited, path, node2route)

        for node, routes in node2route.items():
            for route in routes:
                routeLength = len(route)

                if routeLength < len(longest_route):
                    continue

                if self.checkRouteValid(route):
                    longest_route = route

        return longest_route


def main():
    cstar = Cstar(map.MAP_CONFIG)

    print(cstar.cal_longest_route(0))


if __name__ == "__main__":
    main()
