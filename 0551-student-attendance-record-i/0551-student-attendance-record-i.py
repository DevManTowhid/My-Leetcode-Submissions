class Solution:
    def checkRecord(self, s: str) -> bool:
        counts = {'P': 0, 'L': 0, 'A': 0}
        late_count = 0
        for i in s:
            counts[i] += 1
            if i is not "L":
                late_count = 0
            else:
                late_count += 1
                print(f"Late found consecutive {late_count} day/s")
                if late_count == 3:
                    return False
                
        print(counts)
        if counts['A']:
            if counts['A']>= 2:
                return False

        return True