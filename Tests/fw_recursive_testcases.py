import unittest
import sys

NO_PATH = sys.maxsize

GRAPH = [
        [0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0],
]

MAX_LENGTH = len(GRAPH[0])

def floyd_recursive_shorterpath(distance, intermediate, start_node, end_node):
    if intermediate >= MAX_LENGTH:
        return
    
    if distance[start_node][intermediate] != NO_PATH and distance[intermediate][end_node] != NO_PATH: 
        if distance[start_node][intermediate] + distance[intermediate][end_node] < distance[start_node][end_node]:
            distance[start_node][end_node] = distance[start_node][intermediate] + distance[intermediate][end_node]

    floyd_recursive_shorterpath(distance, intermediate + 1, start_node, end_node)

#above function is used in the floyd_warshall_recursive_solution file


class TestFloydWarshallRecurisve(unittest.TestCase):
    def test_fw_recursive_shorter_path(self):
        distance = [
            [0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
        expected_result = [
            [0, 7, 12, 8],
            [NO_PATH, 0, 5, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
        floyd_recursive_shorterpath(distance, 0, 0, 2)
        self.assertEqual(distance, expected_result)

    # above test is used to test if the path generated is infact the shorter path


    def test_fw_recursive_no_path(self):
        distance = [
            [0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
        expected_result = [
            [0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
        floyd_recursive_shorterpath(distance, 0, 0, 3)
        self.assertEqual(distance, expected_result)

    # above test is used to test if there are no path present between the nodes

    
if __name__ == '__main__':
    unittest.main()