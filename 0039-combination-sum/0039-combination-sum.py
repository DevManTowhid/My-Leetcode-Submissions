class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []

        def backtrack(index, current_path, remaining_target):
            # 1. Base Case: Success! We hit the exact target.
            if remaining_target == 0:
                results.append(list(current_path)) # Append a COPY of the path
                return
            
            # 2. Base Cases: Bust or Out of Bounds
            if remaining_target < 0 or index >= len(candidates):
                return
            
            # --- THE TWO CHOICES ---

            # Choice A: INCLUDE the current number
            current_path.append(candidates[index])
            # Notice we pass 'index' (not index + 1) because we can reuse the number
            backtrack(index, current_path, remaining_target - candidates[index])
            
            # CRITICAL STEP: The actual "Backtrack"
            # We must remove the number we just added before we explore Choice B
            current_path.pop()

            # Choice B: SKIP the current number
            # Move to the next index, leave the path and target exactly as they are
            backtrack(index + 1, current_path, remaining_target)

        # Kick off the recursion starting at index 0, with an empty path
        backtrack(0, [], target)
        return results