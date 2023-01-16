class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:

        @functools.cache
        def func(n):

            s = 0
            for i in range(len(n)):
                s += price[i] * n[i]

            for offer in special:
                if all(x >= y for x, y in zip(n, offer)):
                    s = min(s, offer[~0] + func(tuple(x - y for x, y in zip(n, offer))))

            return s

        return func(tuple(needs))
