# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count/description/

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = defaultdict(int)
        for c in cpdomains:
            count, ud = c.split(" ")
            ds = ud.split(".")
            curr = ""
            for cd in reversed(ds):
                if curr == "":
                    curr += cd
                else:
                    curr = cd + "." + curr

                counter[curr] += int(count)

        res = []
        for k in counter:
            res.append(str(counter[k]) + " " + k)

        return res
    