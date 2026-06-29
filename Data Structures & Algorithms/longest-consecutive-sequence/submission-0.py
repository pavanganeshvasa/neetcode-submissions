class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = defaultdict(set)
        for num in nums:
            if(num  not in hm):
                hm[num].add(num)
            else:
                continue
            if(num-1 in hm):
                hm[num-1].add(num)
            if(num+1 in hm):
                hm[num+1].add(num)

        mx = 0
        for k in hm:
            if(k-1 in hm):
                hm[k].update(hm[k-1])
                hm[k-1] = hm[k]
            if(k+1 in hm):
                hm[k].update(hm[k+1])
                hm[k+1] = hm[k]

            mx = max(mx, len(hm[k]))

        return mx

        