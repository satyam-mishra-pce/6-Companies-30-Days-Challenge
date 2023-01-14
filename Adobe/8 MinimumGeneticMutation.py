class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        minmutations = inf
        def dfs(genestr = start, mutations = 0, visited = set()):
            if genestr == end:
                nonlocal minmutations
                minmutations = min(minmutations, mutations)
            visited.add(genestr)
            for i, genech in enumerate(genestr):
                for mutationch in "ACGT":
                    if genech == mutationch:
                        continue
                    nextgenestr = genestr[:i] + mutationch + genestr[i + 1:]
                    if nextgenestr in bank and nextgenestr not in visited:
                        dfs(nextgenestr, mutations + 1, visited)
        
        dfs()
        if minmutations == inf:
            return -1
        return minmutations

