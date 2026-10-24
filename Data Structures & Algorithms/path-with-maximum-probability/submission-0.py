class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for j in range(len(edges)):
            s,d = edges[j][0], edges[j][1]
            adj[s].append((d,succProb[j]))
            adj[d].append((s,succProb[j]))
        print(adj)
        path = {}
        minHeap = [(-1,start_node)]
        while minHeap:
            w1,n1 = heapq.heappop(minHeap)
            if n1 in path:
                continue
            path[n1] = abs(w1)

            for n2,w2 in adj[n1]:
                if n2 not in path:
                    heapq.heappush(minHeap, (w1*w2, n2))
        print(path)
        if end_node not in path:
            return float(0)
        else:
            return abs(float(path[end_node]))
            
        