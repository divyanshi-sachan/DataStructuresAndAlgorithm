class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False]*n
        queue = [0]
        visited[0] = True
        while queue:
            node = queue.pop()
            for key in rooms[node]:
                if not visited[key]:
                    visited[key] = True
                    queue.append(key)
        return all(visited)
        