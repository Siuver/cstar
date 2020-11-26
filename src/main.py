from map import MAP
from link import LINK
from mytk import MyTk

from cstar import Cstar

def main():
    map_config = get_map_config(LINK, MAP)
    # window = MyTk(map_config)
    cstar = Cstar(map_config)
    print(cstar.cal_longest_route(0), cstar.num)

def get_map_config(link, map):
    for key, value in map.items():
        if int(key) in link:
            link[int(key)]['x'] = int(value['x'])
            link[int(key)]['y'] = int(value['y'])
    return link

if __name__ == "__main__":
    main()