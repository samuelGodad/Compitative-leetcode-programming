class Solution(object):
    def totalFruit(self, tree):
        """
        :type fruits: List[int]
        :rtype: int
        """
        if len(tree) <= 2:
            return len(tree)
        start = 0
        res = 0
        count = {}
        for end in range(len(tree)):
            if tree[end] in count:
                count[tree[end]] += 1
            else:
                count[tree[end]] = 1
            while len(count) > 2:
                count[tree[start]] -= 1
                if count[tree[start]] == 0:
                    del count[tree[start]]
                start += 1
            res = max(res, end - start + 1)
        return res




        
