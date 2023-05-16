graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G', 'H'],
    'D': [],
    'E': ['I', 'J'],
    'F': [],
    'G': ['K', 'M'],
    'H': ['M'],
    'I': ['N', 'P'],
    'J': [],
    'K': ['L'],
    'M': ['Q'],
    'N': [],
    'P': ['R'],
    'L': ['J'],
    'Q': [],
    'R': [],
    'J': [],
}


def dfs(graph, start, goal):
    visited = []
    stack = [[start]]
    while stack:
        path = stack.pop()
        node = path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node in goal:
            return path
        else:
            sub = graph.get(node)
            for snode in sub:
                new_path = path.copy()
                new_path.append(snode)
                stack.append(new_path)


start = input('start: ')
goal = input('goal: ').split()
road = dfs(graph, start, goal)
print('Road is ', road)
