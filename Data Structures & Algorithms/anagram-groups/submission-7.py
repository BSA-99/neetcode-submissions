class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        matchdict = defaultdict(list)
        for i in strs:
            matchdict[(tuple(sorted(i)))].append(i)
        return list(matchdict.values())
            
        
        