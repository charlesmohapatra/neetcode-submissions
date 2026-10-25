class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        for s,d,w in edges:
            adj[s].append((d,w))
            adj[d].append((s,w))
        
        visit = set()
        visit.add(0)
        minHeap = []
        mst = []
        for d1,w1 in adj[0]:
            heapq.heappush(minHeap,(w1,0,d1))
        ans = 0
        while minHeap:
            w1,s1,d1 = heapq.heappop(minHeap)
            if d1 in visit:
                continue
            mst.append((s1,d1))
            visit.add(d1)
            ans += w1
            for d2,w2 in adj[d1]:
                if d2 not in visit:
                    heapq.heappush(minHeap, (w2,s1,d2))
                
        if len(visit) == n:
            return ans
        else:
            return -1

        