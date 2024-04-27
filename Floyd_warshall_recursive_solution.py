import sys

NO_PATH = sys.maxsize

# import sys is used to acces the sys.maxsize rule which identifies the maximum size of integers

GRAPH = [
        [0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0],
]
MAX_LENGTH = len(GRAPH[0])

# MAX_LENGTH identifies the maximum length of the node in the graph

def floyd_recursive(distance, intermediate, start_node, end_node):
    """
    This Function updates the distance in the above Matrix according to 
    Floyd-Warshall Algorithim recursively using the below parameters:

    distance
    intermediate
    start_node
    end_node
    """
    if intermediate >= MAX_LENGTH:
        return
    
    # the above function allows the code to consider all values if the 
    # intermediate is greater than or equal to the MAX_LENGTH value
    
    if distance[start_node][intermediate] != NO_PATH and distance[intermediate][end_node] != NO_PATH: 
        if distance[start_node][intermediate] + distance[intermediate][end_node] < distance[start_node][end_node]:
            distance[start_node][end_node] = distance[start_node][intermediate] + distance[intermediate][end_node]

    # the above function checks if the path shortens the distance between the 
    # start node and the end node through the intermediate to update the graph
    
    floyd_recursive(distance, intermediate + 1, start_node, end_node)

    # the above function allows the code to jumpe to intermediate + 1
    # to check recursively 

def fw_recursive(distance):
    """
    This Function applys the Floyd-Warshall Algorithim to calculate the 
    shortest path between nodes using the distance
    """
    for intermediate in range(MAX_LENGTH):
        for start_node in range(MAX_LENGTH):
            for end_node in range(MAX_LENGTH):
                floyd_recursive(distance, intermediate, start_node, end_node)

# the above function applys the Floyd-Warshall Algorithim
# using the distance as an input 
# it checks all possible intermediates between star node and end node
# to update the graph


fw_recursive(GRAPH)

# the above function Applys the Floyd-Warshall Algorithim to the
# above defined GRAPH


for row in GRAPH:
    for val in row:
        print("NO_PATH" if val == NO_PATH else val, end="\t")
    print()

# the above function prints the result if there is a defined path
# if the path is unreachable the code prints NO_PATH
    