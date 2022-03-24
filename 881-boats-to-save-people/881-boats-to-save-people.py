class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        cnt = 0
        l, r = 0, len(people)-1
        ans = []
        while l <= r:
            if people[l] + people[r] > limit:
                ans.append((people[l],))
                cnt += 1
                l += 1
            else:
                this_sum = people[l]
                this_tup = [people[l]]
                if this_sum + people[r] <= limit:
                    this_tup.append(people[r])
                    r -= 1
                

                ans.append(tuple(this_tup))
                cnt += 1
                l += 1
            # print(l, r, people)
            # print(ans)
        return cnt
                