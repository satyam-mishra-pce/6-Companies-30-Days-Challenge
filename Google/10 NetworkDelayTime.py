class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = dict()
        for u, v, w in times:
            graph[u] = graph.get(u, []) + [(v, w)]
        
        min_dist = [inf] * (n + 1)
        min_dist[k] = 0

        def dfs(u, visited):
            if u not in graph:
                return
            for v, w in graph[u]:
                if v not in visited:
                    new_dist = min_dist[u] + w
                    if new_dist < min_dist[v]:
                        visited.add(v)
                        min_dist[v] = new_dist
                        dfs(v, visited)
                        visited.remove(v)

        dfs(k, {k})
        print(min_dist)

        ret = max(min_dist[1:])
        if ret == inf:
            return -1
        return ret
