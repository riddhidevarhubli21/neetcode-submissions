class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # one for eahc character
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s) #lists cannot be keys so count changes to a tuple
        
        return list(res.values())
        