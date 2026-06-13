class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        n = len(num)

        def dfs(i, expr, total, prev):
            if i == n:
                if total == target:
                    res.append(expr)
                return

            for j in range(i, n):
                if j > i and num[i] == "0":
                    break

                s = num[i:j + 1]
                cur = int(s)

                if i == 0:
                    dfs(j + 1, s, cur, cur)
                else:
                    dfs(j + 1, expr + "+" + s, total + cur, cur)
                    dfs(j + 1, expr + "-" + s, total - cur, -cur)
                    dfs(j + 1, expr + "*" + s, total - prev + prev * cur, prev * cur)

        dfs(0, "", 0, 0)
        return res
