class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for dst, src in prerequisites:
            adj[src].append(dst)
        visit = set()
        hash_set = {}
        for i in range(numCourses):
            if i not in visit:
                self.dfs(i, hash_set, visit, adj)
        answer = []
        for j in queries:
            if j[0] in hash_set[j[1]]:
                answer.append(True)
            else:
                answer.append(False)
        return answer
    def dfs(self, src, hash_set, visit, adj):
        if src not in visit:
            visit.add(src)
            hash_set[src] = set()
        for neighbour in adj[src]:
            if neighbour not in visit:
                self.dfs(neighbour, hash_set, visit, adj)
            hash_set[src].add(neighbour)
            hash_set[src].update(hash_set[neighbour])