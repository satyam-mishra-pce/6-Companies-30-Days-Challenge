class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        if n == 1:
            return 1
        from heapq import heappop, heappush

        graph = dict()
        for city1, city2, time in roads:
            if city1 not in graph:
                graph[city1] = [(city2, time)]
            else:
                graph[city1].append((city2, time))
            
            if city2 not in graph:
                graph[city2] = [(city1, time)]
            else:
                graph[city2].append((city1, time))

        times, ways = [inf] * n, [0] * n
        times[0] = 0
        ways[0] = 1
        stack = [(0,0)]

        while stack:
            time1, city = heapq.heappop(stack)

            for neighbor, time2 in graph[city]:
                if times[neighbor] > time1 + time2:
                    ways[neighbor] = ways[city]
                    times[neighbor] = time1 + time2
                    heapq.heappush(stack,(time1 + time2, neighbor))

                elif times[neighbor] == time1 + time2:
                    ways[neighbor] += ways[city]

        return ways[-1] % (10**9+7)