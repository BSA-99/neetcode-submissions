class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = Counter(nums)
        for number, frequency in count.most_common(k):
            result.append(number)
        return result