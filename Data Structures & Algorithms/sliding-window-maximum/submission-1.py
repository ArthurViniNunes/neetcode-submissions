class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        """Ideia:
            Criar heapmax e ir adicionando e removendo conforme l,r.
        """
        l = 0
        ans = []
        for r in range(k, len(nums)+1):
            heap = nums[l:r]
            heapq.heapify_max(heap)
            ans.append(heapq.heappop_max(heap))
            l += 1
        return ans