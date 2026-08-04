class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def divide_and_conquer(arr):
            if len(arr) == 1 :
                return arr
            if len(arr) == 2:
                if arr[0] > arr[1]: arr = arr[::-1]
                return arr
            
            if len(arr) > 2:
                arrA, arrB = arr[: len(arr) // 2], arr[len(arr) //2 : ]
                arrA = divide_and_conquer(arrA)
                arrB = divide_and_conquer(arrB)
                return merge(arrA, arrB)
            




        
        def merge(arrA, arrB):
            arrA.append(float('inf'))
            arrB.append(float('inf'))
            
            ans = []
            i , j = 0, 0
            while i < len(arrA) and j < len(arrB):
                if arrA[i] <= arrB[j]:
                    ans.append(arrA[i])
                    i += 1
                else:
                    ans.append(arrB[j])
                    j += 1
            if i < len(arrA):
                
                ans += arrA[i:]
            if j < len(arrB):
                
                ans += arrB[j:]
       
            while ans[-1] == float('inf'): ans = ans[:-2]
        
            return ans

        # divide the whole array into halfs
        n = len(nums)
        if n == 1: return nums
        if n == 2: return nums[::-1] if nums[0] > nums[1] else nums
        arrA, arrB = nums[: n // 2], nums[n //2 : ]
        
        arrA = divide_and_conquer(arrA)
        arrB = divide_and_conquer(arrB)
        return merge(arrA, arrB)
        
        