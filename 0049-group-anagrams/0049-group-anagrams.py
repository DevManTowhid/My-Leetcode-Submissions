class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            s2 = "".join(sorted(s))
            if s2 in ans:
                ans[s2].append(s)
            else:
                ans[s2] = [s]
        return list(ans.values())