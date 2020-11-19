MAP_CONFIG = {
    0: {
        'link_node': [1, 3, 6],
        'valid': True
    },
    1: {
        'link_node': [0, 4, 7],
        'valid': True
    },
    2: {
        'link_node': [4, 5],
        'valid': True
    },
    3: {
        'link_node': [0, 5, 6],
        'valid': True
    },
    4: {
        'link_node': [1, 2, 7],
        'valid': True
    },
    5: {
        'link_node': [2, 3, 8, 9],
        'valid': True
    },
    6: {
        'link_node': [0, 3, 9],
        'valid': True
    },
    7: {
        'link_node': [1, 4],
        'valid': True
    },
    8: {
        'link_node': [5],
        'valid': True
    },
    9: {
        'link_node': [5, 6],
        'valid': True
    },
}

node2route = {}


def all_route_to_node(s, e, visited, path):
    visited[s] = True
    path.append(s)

    if s == e:
        if e not in node2route:
            node2route[e] = []
        node2route[e].append(path[:])
    else:
        nodeConfig = MAP_CONFIG[s]
        for linkNode in nodeConfig['link_node']:
            if visited[linkNode] == False and nodeConfig['valid'] == True:
                all_route_to_node(linkNode, e, visited, path)

    path.pop()
    visited[s] = False


def checkRouteValid(route):
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
            for linkNode in MAP_CONFIG[lastNode]['link_node']:
                if linkNode not in closedNode:
                    closedNode.append(linkNode)

        lastNode = passNode

    return valid


def cal_longest_route():
    longest_route = []

    for node in MAP_CONFIG.keys():
        visited = [False] * len(MAP_CONFIG.keys())
        path = []
        all_route_to_node(0, node, visited, path)

    for node, routes in node2route.items():
        for route in routes:
            routeLength = len(route)

            if routeLength < len(longest_route):
                continue

            if checkRouteValid(route):
                longest_route = route

    return longest_route


def main():
    print(cal_longest_route())


if __name__ == "__main__":
    main()
