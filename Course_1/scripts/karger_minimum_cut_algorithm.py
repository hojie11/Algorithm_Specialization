import random
import copy


def mincut(g, t):
    global cuts
    while len(g) > t:
        start = random.choice(list(g.keys()))
        finish = random.choice(g[start])

        for edge in g[finish]:
            if edge != start:
                g[start].append(edge)

        for edge in g[finish]:
            g[edge].remove(finish)
            if edge != start:
                g[edge].append(start)
        del g[finish]

    mincut = len(g[list(g.keys())[0]])
    cuts.append(mincut)

    return graph


graph = {}
cuts = []
edge_list = []

with open('Algorithm_Specialization/Course_1/scripts/src/karger_mincut.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.split('\t')
        node = line[0]
        edges = []
        for edge in line[1:-1]:
            edges.append(edge)
        graph[node] = edges
        edge_list.append(edges)

num_edges = sum(map(len, edge_list))

count = 200
i = 0
while i < count:
    graph1 = copy.deepcopy(graph)
    g = mincut(graph1, 2)
    # g = FastMinCut(graph1)
    i += 1

print("Total edges:     ", num_edges // 2)
print("Total vertices:  ", len(graph))
# print("Maximum degree:  ", max(len(edge_list)))
# print("Minimum degree:  ", min(len(edge_list)))
# print("average degree:  ", sum(len(edge_list)) / len(edge_list))
print("Runing times:    ", len(cuts))
# print() cuts
# print() "Maxcut is", max(cuts)
print("Mincut is        ", min(cuts))