class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.matrix = [[0]*vertices for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.matrix[u][v] = w
        self.matrix[v][u] = w 

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def kruskal_mst(self):
        edges = []

        for i in range(self.V):
            for j in range(i + 1, self.V):
                if self.matrix[i][j] != 0:
                    edges.append((self.matrix[i][j], i, j))

        edges.sort()

        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        mst = []
        total_cost = 0

        for w, u, v in edges:
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                mst.append((u, v, w))
                total_cost += w
                self.union(parent, rank, x, y)

        print("\nEdges in Minimum Cost Spanning Tree:")
        for u, v, w in mst:
            print(f"{u} -- {v} = {w}")
        print("Total cost of MST =", total_cost)


v = int(input("Enter number of vertices: "))
g = Graph(v)

e = int(input("Enter number of edges: "))
print("Enter edges in format: u v w (0-based index)")
for _ in range(e):
    u, v, w = map(int, input().split())
    g.add_edge(u, v, w)

g.kruskal_mst()