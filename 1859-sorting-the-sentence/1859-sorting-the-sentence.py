class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        print(words, len(words))
        ans = [ "" for p in words]
        print(ans)
        for j in words:
            print(int(j[-1]) - 1, j[:-1])
            ans[int(j[-1]) - 1] = j[:-1]
        
        ans = " ".join(c for c in ans)
        
        return ans