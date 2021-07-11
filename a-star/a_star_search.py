import math
from queue import PriorityQueue


def shortest_path(M, start, goal):
    """
    Finds the shortest path from a start node to a goal.

    Args:
      M: Node Map
      start: starting node
      goal: ending node
    Returns:
      A list of nodes in order of traversal (shortest path).
    """

    path = {}
    visited = {start: 0}
    nodes = PriorityQueue()
    nodes.put(start, 0)

    while not nodes.empty():
        current_node = nodes.get()

        for next_node in M.roads[current_node]:
            cost = visited[current_node] + estimate_cost(
                M.intersections[current_node], M.intersections[next_node]
            )

            if next_node not in visited or cost < visited[next_node]:
                visited[next_node] = cost
                path[next_node] = current_node
                nodes.put(next_node, cost)

    return assemble_path(path, start, goal)


def estimate_cost(start_node, end_node):
    """
    Returns the straight line distance between nodes.

    Args:
      start_node: starting node
      end_node: ending node
    Returns:
      Distance between nodes.
    """
    x_dist = start_node[0] - end_node[0]
    y_dist = start_node[1] - end_node[1]

    return math.sqrt(x_dist ** 2 + y_dist ** 2)


def assemble_path(path, start, goal):
    """
    Restructure the final path from a dictionary to a list.

    Args:
      path: dictionary of nodes and their parents
      start: starting node
      goal: ending node
    Returns:
      A list of nodes in order of traversal (shortest path).
    """
    node = goal
    shortest_path = [goal]

    while node != start:
        node = path[node]
        shortest_path.insert(0, node)

    return shortest_path
