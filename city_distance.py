from collections import defaultdict
from math import sqrt


def distance_between_coords(x1, y1, x2, y2):
    """ Find distance between coordinates"""
    distance = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return distance


def name_coords(coords):
    """ Compute coords count. """
    coord_count = 0
    for coord in coords:
        coord_count += 1
        coord.append(coord_count)
    return coords


def graph(coords):
    """ Build graph with nodes and edges. """
    coords = name_coords(coords)
    _graph = defaultdict(list)
    _edges = {}
    for current in coords:
        for comparer in coords:
            if comparer == current:
                continue
            else:
                weight = distance_between_coords(current[0], current[1],
                                                 comparer[0], comparer[1])
                _graph[current[2]].append(comparer[2])
                _edges[current[2], comparer[2]] = weight
    return coords, _edges


def shortest_path(node_list, _edges, start):
    """ Finds shortest path between nodes and edges with start node."""
    unvisited = []
    visited = []
    current_node = start
    for node in node_list:
        if node[2] == start:
            visited.append(start)
        else:
            unvisited.append(node[2])
    while unvisited:
        for index, neighbor in enumerate(unvisited):
            if index == 0:
                current_weight = _edges[start, neighbor]
                current_node = neighbor
            elif _edges[start, neighbor] < current_weight:
                current_weight = _edges[start, neighbor]
                current_node = neighbor
        unvisited.remove(current_node)
        visited.append(current_node)
    return visited


if __name__ == '__main__':
    print("Note: Accepts inputs with comma separated floating point values")
    city_a_lat, city_a_lng = map(float, input('City A : ').split(','))
    city_b_lat, city_b_lng = map(float, input('City B : ').split(','))
    city_c_lat, city_c_lng = map(float, input('City C : ').split(','))
    city_d_lat, city_d_lng = map(float, input('City D : ').split(','))

    coordinates = [[city_a_lat, city_a_lng], [city_b_lat, city_b_lng],
                   [city_c_lat, city_c_lng], [city_d_lat, city_d_lng]
                   ]
    coordinates, edges = graph(coordinates)
    path = shortest_path(coordinates, edges, 1)
    mapping = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}
    print(f"{[mapping[p] for p in path]}")
