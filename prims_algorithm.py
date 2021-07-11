import heapq # PriorityQueue


def create_graph(num_islands, bridge_config):
    """
    Helper function to create graph using adjacency list implementation
    """
    graph = [list() for _ in range(num_islands + 1)]
    
    # populate the adjacency_list
    for config in bridge_config:
        source = config[0]
        destination = config[1]
        cost = config[2]
        
        # An entry in a sublist of graph is represented as a tuple (neighbor, edge_cost)
        graph[source].append((destination, cost))
        graph[destination].append((source, cost))
           
    return graph

def minimum_cost(graph):
    """
    Helper function to find minimum cost of connecting all islands
    """
    # start with vertex 1 (any vertex can be chosen)
    start_vertex = 1
    visited = [False for _ in range(len(graph) + 1)]
    
    # A node in heap is represented as tuple (edge_cost, neighbor)
    minHeap = [(0, start_vertex)]
    total_cost = 0

    while len(minHeap) > 0:
        # heapq.heappop() automatically pops node with the smallest edge_cost, reducing the heap size
        cost, current_vertex = heapq.heappop(minHeap)
        
        if visited[current_vertex]:
            continue

        total_cost += cost

        for neighbor, edge_cost in graph[current_vertex]:
            heapq.heappush(minHeap, (edge_cost, neighbor))

        visited[current_vertex] = True

    return total_cost


"""
:param: num_islands - number of islands
:param: bridge_config - bridge configuration
return: cost (int) minimum cost of connecting all islands
"""
def get_minimum_cost_of_connecting(num_islands, bridge_config):
    graph = create_graph(num_islands, bridge_config)
    return minimum_cost(graph)


def test_function(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = get_minimum_cost_of_connecting(num_islands, bridge_config)
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")


num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
solution = 6

test_case = [num_islands, bridge_config, solution]
test_function(test_case)

num_islands = 5
bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]
solution = 13

test_case = [num_islands, bridge_config, solution]
test_function(test_case)

num_islands = 5
bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
solution = 31

test_case = [num_islands, bridge_config, solution]
test_function(test_case)

# -------------------------
# Uncomment to demo minHeap
# minHeap = list()

# heapq.heappush(minHeap, 5)
# heapq.heappush(minHeap, 6)
# heapq.heappush(minHeap, 2)
# heapq.heappush(minHeap, 1)
# heapq.heappush(minHeap, 9)

# print("After pushing, heap looks like: {}".format(minHeap))

# # pop and return smallest element from the heap
# smallest = heapq.heappop(minHeap)   

# print("Smallest element in the original list was: {}".format(smallest))
# print("After popping, heap looks like: {}".format(minHeap))

# minHeap = list()

# heapq.heappush(minHeap, (0, 1))
# heapq.heappush(minHeap, (-1, 5))
# heapq.heappush(minHeap, (2, 0))
# heapq.heappush(minHeap, (5, -1))

# print("After pushing, now heap looks like: {}".format(minHeap))

# # pop and return smallest element from the heap
# smallest = heapq.heappop(minHeap)   

# print("Smallest element in the original list was: {}".format(smallest))
# print("After popping, heap looks like: {}".format(minHeap))
