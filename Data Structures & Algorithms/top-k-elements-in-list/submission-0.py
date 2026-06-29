class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res =  Counter(nums).most_common(k)
        p = []
        for n in res:
            p.append(n[0])
        
        return p

        