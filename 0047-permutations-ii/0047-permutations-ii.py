class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backTracking(path, remaining):

            if not remaining:
                results.append(path.copy())
                return

            used = set()

            for j in range(len(remaining)):

                if remaining[j] in used:
                    continue

                used.add(remaining[j])

                backTracking(
                    path + [remaining[j]],
                    remaining[:j] + remaining[j + 1:]
                )

        backTracking([], nums)

        return results


