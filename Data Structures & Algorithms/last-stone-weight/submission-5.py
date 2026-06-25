class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap)>=2:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            if first == second:
                continue
            else:
                heapq.heappush(heap, first - second)
        if len(heap)==1:
            return -heap[0]
        else:
            return 0




        