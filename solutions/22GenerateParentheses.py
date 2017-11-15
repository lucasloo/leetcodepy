#  Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(results, currentStr, currentLeft, currentRight):
            if currentLeft == 0 and currentRight == 0:
                results.append(currentStr)
            else:
                if currentLeft > 0:
                    generate(results, currentStr + "(", currentLeft - 1, currentRight + 1)
                if currentRight > 0:
                    generate(results, currentStr + ")", currentLeft, currentRight - 1)
        currentLeft, currentRight = n, 0
        results = []
        currentStr = ""
        generate(results, currentStr, currentLeft, currentRight)
        return results


# quickest solution record
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # record result from 0,1,2,...,n, total n+1 results
        res = [[] for _ in range(n+1)]
        res[0].append('')
        
        for i in range(n+1):
            for j in range(i):
                res[i] += ['(' + x + ')' + y for x in res[j] for y in res[i-j-1]]
        return res[n]
