from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0:
            return []

        # Count frequencies
        freq_map = Counter(nums)

        # Use a max heap (negative frequency for max behavior)
        heap = [(-count, num) for num, count in freq_map.items()]
        heapq.heapify(heap)

        # Extract top k elements
        result = []
        for _ in range(min(k, len(heap))):
            count, num = heapq.heappop(heap)
            result.append(num)

        return result
