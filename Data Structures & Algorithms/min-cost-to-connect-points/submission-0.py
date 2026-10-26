class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}
        nodes = {}
        for i in range(len(points)):
            nodes[i] = points[i]
        for i in range(len(points)):
            adj[i] = []

        for i in range(len(nodes)):
            for j in range(i, len(nodes)):
                distance = abs(nodes[i][0] - nodes[j][0]) + abs(nodes[i][1]-nodes[j][1])
                adj[i].append([j, distance])
                adj[j].append([i, distance])
        visit = set()
        minHeap = []
        for d,w in adj[0]:
            heapq.heappush(minHeap, (w, 0, d))
        visit.add(0)
        ans = 0
        while minHeap:
            w1,s1,d1 = heapq.heappop(minHeap)
            if d1 in visit:
                continue
            visit.add(d1)
            ans += w1
            for d2,w2 in adj[d1]:
                if d2 not in visit:
                    heapq.heappush(minHeap, (w2,d1,d2))
        return ans
                


        