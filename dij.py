# !/usr/bin/python3
# -*-coding:utf-8-*-


def dijkstra(graph, src):
    if graph is None:
        return None
    nodes = [i for i in range(len(graph))]
    distance = {}
    path = {}
    forwarding_table = {}
    source_node = src

    # store the appended node
    exist_node = set()
    exist_node.add(source_node)

    # initial the ini_node, the first step
    for index, ini_dis in enumerate(graph[source_node]):
        distance[index] = ini_dis
        if ini_dis != float('inf'):
            forwarding_table[index] = None
        else:
            forwarding_table[index] = source_node

    # the loop
    adj_node = select_a_related_node(graph[source_node], exist_node)
    while len(exist_node) != len(nodes):
        adj_distance_list = graph[adj_node]
        exist_node.add(adj_node)

        # find the adjacent node and ignore the float('inf') node
        for index, adj_dis in enumerate(adj_distance_list):
            if adj_dis is not float('inf'):
                exist_distance = distance[adj_node]
                if exist_distance + graph[adj_node][index] < distance[index]:
                    distance[index] = exist_distance + graph[adj_node][index]
                    forwarding_table[index] = adj_node
            else:
                continue
        adj_node = select_a_related_node(graph[adj_node], exist_node)

        # format the path
        format_the_path(forwarding_table, path, nodes)

    return distance, path, forwarding_table


# find the related adjacent node of the node
def select_a_related_node(distance_list, exist_node):
    for index, distance in enumerate(distance_list):
        if (distance is not float("inf")) and (index not in exist_node):
            return index


# format the path string
def format_the_path(forwarding_table, path, nodes):
    for index in range(len(nodes)):
        node = index
        path_format_str = ' ---> {}'.format(node)
        while forwarding_table[node] is not None:
            node = forwarding_table[node]
            path_format_str = ' ---> {}'.format(node) + path_format_str
        path_format_str = '{}'.format(src) + path_format_str
        path[index] = path_format_str


if __name__ == "__main__":
    graph_list = [
        [0, 7, float('inf'), 3, 3, 2],
        [7, 0, 5, float('inf'), 1, 2],
        [float('inf'), 5, 0, 6, float('inf'), 3],
        [3, float('inf'), 6, 0, float('inf'), 1],
        [3, 1, float('inf'), float('inf'), 0, float('inf')],
        [2, 2, 3, 1, float('inf'), 0],
    ]
    src = input('please input the source node')
    print('the source node is {} '.format(src))
    distance, path, forwarding_table = dijkstra(graph_list, int(src))
    print(distance)
    print(path)
    print(forwarding_table)
