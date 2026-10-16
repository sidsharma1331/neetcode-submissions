class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        heap = [(0,k)]
        visited = {}
        while heap:
            dist, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited[node] = dist
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (dist+weight, neighbor))
        if len(visited)!=n:
            return -1
        return max(visited.values())
        