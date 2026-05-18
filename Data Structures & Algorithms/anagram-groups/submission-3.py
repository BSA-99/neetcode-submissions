class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        match_dict = defaultdict(list)
        for i in strs:
            match_dict[tuple(sorted(i))].append(i)

        return list(match_dict.values())
        
        