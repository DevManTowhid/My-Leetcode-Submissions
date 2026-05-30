class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []
        # Sorting is absolutely critical here to group duplicates together
        candidates.sort() 
        
        def backtrack(index, current_path, remaining_target):
            # 1. Base Case: Success!
            if remaining_target == 0:
                results.append(list(current_path))
                return
            
            # 2. Base Cases: Bust or Out of Bounds
            if remaining_target < 0 or index >= len(candidates):
                return
            
            # --- THE TWO CHOICES ---

            # Choice A: INCLUDE the current number
            current_path.append(candidates[index])
            # Move to index + 1 because we can only use each number ONCE
            backtrack(index + 1, current_path, remaining_target - candidates[index])
            # The crucial backtrack step to remove the number before Choice B
            current_path.pop() 

            # Choice B: SKIP the current number
            # To avoid duplicate combinations, if we skip a number, 
            # we MUST skip all identical numbers right next to it.
            next_index = index + 1
            while next_index < len(candidates) and candidates[next_index] == candidates[index]:
                next_index += 1
                
            # Move forward using our new skipped index
            backtrack(next_index, current_path, remaining_target)

        # Kick off the recursion
        backtrack(0, [], target)
        return results