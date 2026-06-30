class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxFreq = max(freq.values())
        tail = list(freq.values()).count(maxFreq)

        formula = (maxFreq-1)*(n+1)+tail
        task = len(tasks)

        return max(formula, task)

        
        