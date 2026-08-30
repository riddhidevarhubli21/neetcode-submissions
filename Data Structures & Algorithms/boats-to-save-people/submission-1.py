class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        m = max(people)
        count = [0] * (m + 1)

        for p in people:
            count[p] += 1

        idx, i = 0, 1
        while idx < len(people):
            while count[i] == 0:
                i += 1
            people[idx] = i
            count[i] -= 1
            idx += 1
        
        res, l, r = 0, 0 , len(people) - 1
        while l <= r:
            remaining = limit - people[r]
            #heaviest person first, so move r inwards
            r -= 1
            res += 1
            #trying to pair l with someone
            if l <=r and remaining >=people[l]:
                l += 1
        return res
        