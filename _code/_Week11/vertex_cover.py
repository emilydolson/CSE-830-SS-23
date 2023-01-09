nodes = int(input())
edges = int(input())

def is_solved(included, graph):
    covered = set()
    for v in included:
        covered.add(v)
        for adj in graph[v]:
            covered.add(adj)

    return len(covered) == nodes

best = float("inf")

def vertex_cover(included, vertices, graph):
    global best

    if is_solved(included, graph):
        # print(included)
        if len(included) < best:
            best = len(included)
        return len(included)

    if len(vertices) == 0:
        return float("inf")

    if len(included) >= best - 1:
        return best

    if not is_solved(included + vertices, graph):
        return float("inf")

    next_vertex = vertices.pop()
    incl_list = included[:]
    incl_list.append(next_vertex)
    incl_result = vertex_cover(incl_list, vertices[:], graph)
    excl_result = vertex_cover(included[:], vertices[:], graph)

    return min(incl_result, excl_result)
    

graph = {}

for i in range(nodes):
    graph[i] = []

for i in range(edges):
    e = [int(v) for v in input().split(" ")]
    graph[e[0]].append(e[1])
    graph[e[1]].append(e[0])

included = []
vertices_to_consider = [i for i in range(nodes)]
for node in graph.keys():
    if len(graph[node]) == 1:
        if not graph[node][0] in included:
            included.append(graph[node][0])
            vertices_to_consider.remove(graph[node][0])
            vertices_to_consider.remove(node)
            
# vertices_to_consider.sort(key=lambda x: len(graph[x]))
print(vertex_cover(included, vertices_to_consider, graph))
