class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-x for x in nums]
        heapq.heapify(heap)
        l1 = []

        for i in range(k):
            result = heapq.heappop(heap)

        return -result




        