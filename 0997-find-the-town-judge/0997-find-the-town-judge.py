class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        people = set()
        trusts = dict()
        trusted = dict()
        for i , j in trust:
            people.add(i)
            people.add(j)
            if i not in trusts.keys():
                trusts[i] = 1

            else: trusts[i] += 1
            if j not in trusted.keys():
                trusted[j] = 1
            else: trusted[j] += 1
            
            
            

            
        print("all: ", people)
        print("Total people: ", len(people))
        print("Trusts: ", list(trusts.keys()))
        print("Trusted: ", list(trusted.keys()))

        
        
        town_judge = [i for i in people if  i not in trusts.keys() and trusted[i] == (len(people) - 1)]
        ans = town_judge[0] if town_judge else -1

        print(ans)
        return ans
             
            
        