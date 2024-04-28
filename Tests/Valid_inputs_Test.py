import sys
import Floyd_warshall_recursive_solution


def validate_graph_input(GRAPH):
    for row in GRAPH:
        for val in row:
            if not isinstance(val, int):
                raise ValueError("Graph must contain only integers")

# the above function ensures that the only allowed inputs are integers


NO_PATH = sys.maxsize

GRAPH = [
        [0, "A", NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0],
]

validate_graph_input(GRAPH)