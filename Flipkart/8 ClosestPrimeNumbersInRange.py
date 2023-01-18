class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        import array
        from math import sqrt

        def getPrimes(n):
            # Sieve of Eratosthenes
            binary = [1] * (n + 1)
            
            i = 2
            while i * i <= n:
                j = i
                while j * i <= n:
                    binary[j * i] = 0
                    j += 1
                i += 1
            
            binary[0] = 0
            binary[1] = 0
            
            return binary

        def getPrimesInRange(low, high):
            # Segmented Sieve of Eratosthenes
            responsibles = getPrimes(int(sqrt(high)) + 1)
            binary = [1] * (high + 1 - low)
            
            for factor, isfactor in enumerate(responsibles):
                if isfactor:
                    multiple = low - (low % factor)
                    if multiple < low:
                        multiple += factor 
                    while multiple <= high:
                        if multiple != factor:
                            binary[multiple - low] = 0
                        multiple += factor
            if low < 2:
                binary[0] = 0
            if low == 0:
                binary[1] = 0
            return binary

        ret = [-1, -1]
        lastprime = 0
        for prime, isPrime in enumerate(getPrimesInRange(left, right), left):
            if isPrime:
                if ret[0] == -1:
                    ret[0] = prime
                elif ret[1] == -1:
                    ret[1] = prime
                elif prime - lastprime < ret[1] - ret[0]:
                    ret[0] = lastprime
                    ret[1] = prime
                lastprime = prime
        if ret[1] == -1:
            return [-1, -1]
        return ret
