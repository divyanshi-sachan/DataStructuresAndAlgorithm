import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        pq = [(0, 0, 1)]
        while pq:
            d, node, count = heapq.heappop(pq)
            if d != dist[node][count]:
                continue
            if node == n - 1:
                return d
            for nei, weight in graph[node]:
                if labels[node] == labels[nei]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue
                new_dist = d + weight
                if new_dist < dist[nei][new_count]:
                    dist[nei][new_count] = new_dist
                    heapq.heappush(
                        pq,
                        (new_dist, nei, new_count)
                    )
        return -1