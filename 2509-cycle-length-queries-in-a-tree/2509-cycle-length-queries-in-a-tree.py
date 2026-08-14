class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res = [0 for p in queries]
        for index, i in enumerate(queries):
            stack1 = []
            stack2 = []
            level_a, level_b = int(math.log2(i[0])), int(math.log2(i[1])) 
            p, q = i[0], i[1]
            while p >= 1:
                stack1.append(p)
                p = p // 2
            while q >= 1:
                stack2.append(q)
                q = q // 2
            # print(f'path to the {i[0]}: ', stack1[::-1] )
            # print(f'path to the {i[1]}: ', stack2[::-1] )

            a, b = stack1.pop(), stack2.pop()
            while stack1 and stack2:
                c, d = stack1.pop(), stack2.pop()
                if c == d:
                    a, b = c, d
                else:
                    break
            
                

            

            # print(a, b)

            lca_level = int(math.log2(a))
            # print(lca_level)

            res[index] = level_a + level_b - (2 * lca_level)  +  1
        
        return res
            
        

        