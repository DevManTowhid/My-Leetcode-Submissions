from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)
        res = []
        extras = [p for p in arr1 if p not in arr2]
        extras.sort()
        freq_extras = Counter(extras)
        for j in arr2:
            res += [j] * freq[j]
        for j in freq_extras.keys():
            res += [j] * freq_extras[j]
        
        return res
            
        