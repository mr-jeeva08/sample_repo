import heapq

def astar(start, goal, graph, heuristic, max_nodes=None):
    heap = [(0, start)]
    visited = set()
    came_from = {}
    cost_so_far = {}

    came_from[start] = None
    cost_so_far[start] = 0

    if max_nodes is None:
        max_nodes = float('inf')

    count = 0

    while heap and count < max_nodes:
        count += 1
        current = heapq.heappop(heap)[1]

        if current == goal:
            break

        if current in visited:
            continue

        visited.add(current)

        for next_node, weight in graph[current]:
            new_cost = cost_so_far[current] + weight

            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic(goal, next_node)
                heapq.heappush(heap, (priority, next_node))
                came_from[next_node] = current

    return came_from, cost_so_far


# ------------------ Graph Data ------------------

start = 'A'
goal = 'G'

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('D', 2), ('E', 4)],
    'C': [('A', 3), ('F', 5)],
    'D': [('B', 2)],
    'E': [('B', 4), ('G', 2)],
    'F': [('C', 5)],
    'G': [('E', 2)]
}

def heuristic(goal, node):
    return abs(ord(goal) - ord(node))

max_nodes = 10

came_from, cost_so_far = astar(start, goal, graph, heuristic, max_nodes)

print("Came from:", came_from)
print("Cost so far:", cost_so_far)
