from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Map will store: { tuple_of_sorted_chars : [list_of_original_strings] }
        anagram_map = defaultdict(list)
        
        for s in strs:
            # 1. Sort the string
            # 2. Convert the resulting list into a tuple (which is hashable)
            sorted_key = tuple(sorted(s))
            
            # 3. Append the original string to the corresponding group
            anagram_map[sorted_key].append(s)
            
        # Return all the grouped lists
        return list(anagram_map.values())