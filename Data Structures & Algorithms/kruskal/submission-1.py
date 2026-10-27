class UnionFind:
    def __init__(self,n):
        self.rank = {}
        self.par = {}
        for i in range(n):
            self.rank[i] = 0
            self.par[i] = i
    def find(self,j):
        if self.par[j] != j:
            self.par[j] = self.find(self.par[j])
        return self.par[j]
    def union(self, n1, n2):
        p1,p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        elif self.rank[p1] == self.rank[p2]:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minHeap = []
        for s,d,w in edges:
            heapq.heappush(minHeap, (w,s,d))
        unionFind = UnionFind(n)
        mst = []
        ans = 0
        while len(mst) < n-1 and minHeap:
            w1,s1,d1 = heapq.heappop(minHeap)
            if not unionFind.union(s1,d1):
                continue
            ans += w1
            mst.append([s1,d1])
        if len(mst) == n-1:
            return ans
        else: 
            return -1
