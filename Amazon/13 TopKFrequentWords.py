class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        from heapq import heapify, heappop
        frequency_map = dict()

        for word in words:
            if word not in frequency_map:
                frequency_map[word] = 1
            else:
                frequency_map[word] += 1
        
        word_heap = [(-frequency_map[word], word) for word in frequency_map]
        heapify(word_heap)

        ret = []
        for i in range(k):
            ret.append(heappop(word_heap)[1])
        return ret