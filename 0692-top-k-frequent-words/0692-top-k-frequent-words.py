
        
from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words or k <= 0:
            return []

        # Count frequencies
        freq_map = Counter(words)

        # Use a max heap (negative frequency for max behavior)
        heap = [(-count, word) for word, count in freq_map.items()]
        heapq.heapify(heap)

        # Extract top k elements
        result = []
        for _ in range(min(k, len(heap))):
            count, num = heapq.heappop(heap)
            result.append(num)

        return result



