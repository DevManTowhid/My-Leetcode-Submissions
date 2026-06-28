class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def normalizeIndices(arr):
            arr = sorted(arr)
            arr = [value for value in arr if value != -1]
            
            return [arr[0], arr[-1]] if arr else [-1, -1]


        def searchfirstlast(arr, left, right, target):
            # for blank arrays
            if not arr:
                return [-1, -1]

            # for single element arrays

            if left == right:
                return [left, right] if arr[left] == target else [-1, -1]

            # for 2 elements arrays

            if left + 1 == right:
                if arr[left] != target and arr[right] != target:
                    return [-1, -1]
                if arr[left] == arr[right] and arr[left] == target: return [left, right]
                else:
                    return [left, left] if arr[right] != target else [right, right]

            mid_1 = ((right + left) // 2)
            mid = max(left, mid_1 - 1)
            if arr[mid] == arr[mid_1] and arr[mid] == target:
                left_indices = searchfirstlast(arr, left, mid, target)
                right_indices = searchfirstlast(arr, mid_1, right, target)
                return normalizeIndices(left_indices + right_indices)
            else:
                if arr[mid] >= target:
                    left_indices = searchfirstlast(arr, left, mid, target)
                    return left_indices

                elif arr[mid + 1] <= target:
                    right_indices = searchfirstlast(arr, mid + 1, right, target)
                    return right_indices
                return [-1, - 1]

        return searchfirstlast(nums, 0, len(nums) - 1, target)






        