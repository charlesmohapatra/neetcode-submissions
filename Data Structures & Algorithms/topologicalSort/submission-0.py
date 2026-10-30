class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        for src, dst in edges:
            adj[src].append(dst)
        topSort = []
        visit = set()
        cycle = set()
        for i in range(n):
            if not self.dfs(i, adj, topSort, visit, cycle):
                return []
        topSort.reverse()
        return topSort
    
    def dfs(self, src, adj, topSort, visit, cycle):
        if src in cycle:
            return False
        if src in visit:
            return True
        visit.add(src)
        cycle.add(src)
        for neighbour in adj[src]:
            if not self.dfs(neighbour, adj, topSort, visit, cycle):
                return False
        cycle.remove(src)
        topSort.append(src)
        return True