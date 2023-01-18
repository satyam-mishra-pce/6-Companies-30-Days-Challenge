class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        if len(barcodes) == 1:
            return barcodes
        
        from heapq import heapify, heappop, heappush

        freq_map = dict()
        for code in barcodes:
            if code not in freq_map:
                freq_map[code] = -1
            else:
                freq_map[code] -= 1
        
        freq_heap = [(freq_map[code], code) for code in freq_map]
        heapify(freq_heap)

        print(freq_heap)
        def recursion(arr = [], heap = freq_heap):
            if not heap:
                return arr
            if len(heap) == 1:
                arr.append(heap[0][1])
                return arr
            max1 = heappop(heap)
            max2 = heappop(heap)
            arr.extend([max1[1], max2[1]])
            max1 = (max1[0] + 1, max1[1])
            max2 = (max2[0] + 1, max2[1])
            if max1[0]:
                heappush(heap, max1)
            if max2[0]:
                heappush(heap, max2)
            
            return recursion(arr, heap)

        return recursion()
