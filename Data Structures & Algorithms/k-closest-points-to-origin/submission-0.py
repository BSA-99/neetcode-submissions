class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = [(p[0]**2 + p[1]**2, (p[0],p[1])) for p in points]
        heapq.heapify(heap)
        l1 = []

        for i in range(k):
            result = heapq.heappop(heap)
            point = result[1]
            l1.append(list(point))
        
        return l1

        



        
        