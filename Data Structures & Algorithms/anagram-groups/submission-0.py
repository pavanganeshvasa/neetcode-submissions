from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        res = []

        for s in strs:
            ctr = Counter(s);
            k = tuple(sorted(ctr.items()))
            hm[k].append(s)


        for key in hm:
            res.append(hm[key])


        return res


        