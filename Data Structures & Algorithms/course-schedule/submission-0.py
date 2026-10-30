class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for src, dst in prerequisites:
            adj[src].append(dst)
        visit = set()
        cycle = set()
        for i in range(numCourses):
            if not self.dfs(i,adj,visit,cycle):
                return False
        return True
    
    def dfs(self, src, adj, visit, cycle):
        if src in cycle:
            return False
        if src in visit:
            return True
        visit.add(src)
        cycle.add(src)
        for neighbour in adj[src]:
            if not self.dfs(neighbour, adj, visit, cycle):
                return False
        cycle.remove(src)
        return True
        