class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in groups:
                groups[key]=[]
            groups[key].append(word)
        return list(groups.values())


    def isAnagram(self, s: str, t: str) -> bool:
        sort_s = "".join(sorted(s))
        sort_t = "".join(sorted(t))
        if (sort_s == sort_t):
            return True
        else : 
            return False