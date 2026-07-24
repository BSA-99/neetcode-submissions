class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = Counter(nums)
        for pairs in count.most_common(k):
            result.append(pairs[0])
        return result