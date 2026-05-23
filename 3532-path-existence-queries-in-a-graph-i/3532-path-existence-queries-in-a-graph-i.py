class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        componentID = [0] * n
        componentId = 0
        answer = [False] * len(queries) 
        for i in range(len(nums)):
    
            if i > 0 and nums[i] - nums[i-1] > maxDiff:
                
                componentId += 1
            componentID[i] = componentId
            
            
        for i in range(len(queries)):
           
            answer[i] = True if componentID[queries[i][0]] == componentID[queries[i][1]] else False

        return answer
