class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if prerequisites == []:
            return True

        taken = [0] * numCourses
        coursemap = dict()
        for ai, bi in prerequisites:
            if ai not in coursemap:
                coursemap[ai] = [bi]
            else:
                coursemap[ai].append(bi)
        
        def dfs(u, dependent):
            if taken[u]:
                return True
            if u in coursemap:
                dependent.add(u)
                for v in coursemap[u]:
                    if v in dependent:
                        return False
                    else:
                        if not dfs(v, dependent):
                            return False
                dependent.remove(u)
            taken[u] = 1
            return True
        
        for need in range(numCourses):
            dfs(need, set())
        
        return not(0 in taken)