# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# For example:
# Given "25525511135",
#
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)


class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(l, s):
            if len(l) > 4:
                return
            elif len(l) == 4 and len(s) == 0:
                res.append([".".join(x) for x in l])
            elif len(s) == 0:
                return
            else:
                lastDigit = l[-1] if len(l) > 0 else None
                if not lastDigit or l[-1] * 10 + int(s[0]) > 255:  # None or 0
                    dfs(l + [int(s[0])], s[1:])
                else:
                    dfs(l + [int(s[0])], s[1:])
                    dfs(l[0:-1] + [l[-1] * 10 + int(s[0])], s[1:])
        res = []
        dfs([], s)
        return res

a = Solution()
print(a.restoreIpAddresses("2552550135"))
