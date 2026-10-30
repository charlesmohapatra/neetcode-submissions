class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for src, dst in prerequisites:
            adj[src].append(dst)
        visit = set()
        cycle = set()
        topSort = []
        for i in range(numCourses):
            if not self.dfs(i,adj,visit,cycle, topSort):
                return []
        return topSort
    
    def dfs(self, src, adj, visit, cycle, topSort):
        if src in cycle:
            return False
        if src in visit:
            return True
        visit.add(src)
        cycle.add(src)
        for neighbour in adj[src]:
            if not self.dfs(neighbour, adj, visit, cycle, topSort):
                return False
        topSort.append(src)
        cycle.remove(src)
        return True
        