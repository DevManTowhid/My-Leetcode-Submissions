from typing import List
from collections import Counter
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        freq_map = Counter(s)
        print(freq_map)
        sorted_items = sorted(freq_map.items(), key=lambda item: item[1], reverse=True)
        print(sorted_items)
        ans = ""
        for x in sorted_items:
            ans += x[0] * x[1]
        return ans

        