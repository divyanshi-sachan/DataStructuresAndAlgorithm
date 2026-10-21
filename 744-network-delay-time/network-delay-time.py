import heapq
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        dist = [float('inf')]*(n+1)
        dist[k] = 0
        heap = [(0,k)]
        while heap:
            d,node = heapq.heappop(heap)
            if d>dist[node]:
                continue
            for neighbour,weight in graph[node]:
                new_dist = d+weight
                if new_dist<dist[neighbour]:
                    dist[neighbour] = new_dist
                    heapq.heappush(heap,(new_dist,neighbour))
        answer = max(dist[1:])
        return answer if answer!=float('inf') else -1

        