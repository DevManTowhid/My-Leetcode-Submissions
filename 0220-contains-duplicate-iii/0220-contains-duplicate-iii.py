from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False

        bucket_size = valueDiff + 1  # Avoid division by zero
        buckets = {}

        def get_bucket_id(x):
            return x // bucket_size

        for i, num in enumerate(nums):
            bucket_id = get_bucket_id(num)

            # Case 1: Same bucket
            if bucket_id in buckets:
                return True

            # Case 2: Neighboring buckets
            if (bucket_id - 1 in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff):
                return True
            if (bucket_id + 1 in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff):
                return True

            # Insert into bucket
            buckets[bucket_id] = num

            # Maintain sliding window of size indexDiff
            if i >= indexDiff:
                old_bucket_id = get_bucket_id(nums[i - indexDiff])
                del buckets[old_bucket_id]

        return False
