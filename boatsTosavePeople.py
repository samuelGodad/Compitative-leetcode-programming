class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        ret = 0
        q = deque(sorted(people))
        while q:
            tail = q.pop()
            ret += 1
            if q and q[0] + tail <= limit:
                q.popleft()

        return ret
    
