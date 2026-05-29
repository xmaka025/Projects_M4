from collections import deque


class Node:
    def __init__(self, value):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({self.value})'


class Graph:
    def __init__(self, root):
        self._root = root

    def dfs(self):
        visited = set()
        result = []

        def dfs1(node):
            visited.add(node)
            print(node.value)
            result.append(node.value)

            for neighbor in node.outbound:
                if neighbor not in visited:
                    dfs1(neighbor)
        dfs1(self._root)
        return result
    def bfs(self):
        visited = set()
        queue = deque()
        result = []

        queue.append(self._root)
        visited.add(self._root)

        while queue:
            vertex = queue.popleft()
            print(vertex.value)
            result.append(vertex.value)

            for neighbor in vertex.outbound:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return result


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)

g = Graph(a)


print(g.dfs())

print(g.bfs())
