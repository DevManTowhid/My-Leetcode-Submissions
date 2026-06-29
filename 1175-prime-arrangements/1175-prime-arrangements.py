class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def permutation(n):
            return math.factorial(n)

        modulo = 1000000007
        prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (prime[p] == True):
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
        primes =  [p for p in range(2, n + 1) if prime[p] and p != 0]
        total_primes = len(primes)
        non_primes = (len(prime) - 1) - len(primes) 
        print(primes, total_primes, non_primes)
        result = ((permutation(total_primes) % modulo) * (permutation(non_primes) % modulo))   % modulo
        return result

        



