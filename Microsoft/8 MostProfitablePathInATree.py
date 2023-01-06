class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        
        n = len(edges) + 1
        tree = [[] for _ in range(n)]
        for edge1, edge2 in edges:
            tree[edge1].append(edge2)
            tree[edge2].append(edge1)
        
        visited = [0] * n

        def dfs(node, root_dist):
            visited[node] = 1
            dist = -inf
            bob_dist = n
            if node == bob:
                bob_dist = 0
            for nextnode in tree[node]:
                if visited[nextnode]:
                    continue
                new_dist, new_bob_dist = dfs(nextnode, root_dist + 1)
                dist = max(dist, new_dist)
                bob_dist = min(bob_dist, new_bob_dist)
            if dist == -inf:
                dist = 0
            if root_dist == bob_dist:
                dist += amount[node] // 2
            if root_dist < bob_dist:
                dist += amount[node]
            return dist, bob_dist + 1

        return dfs(0, 0)[0]