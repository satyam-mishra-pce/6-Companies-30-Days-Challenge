class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        ans = []
        def recursion(curr, dotindices = list()):

            if len(dotindices) == 3:
                if 1 <= len(s) - curr <= 3 and not(len(s) - curr > 1 and s[curr :].startswith("0")) and int(s[curr :]) <= 255:
                    ip_string = ""
                    for i in range(3):
                        if not i:
                            ip_string += s[:dotindices[0]] + "."
                        else:
                            ip_string += s[dotindices[i - 1] : dotindices[i]] + "."
                        
                    ip_string += s[dotindices[~0] :]
                    ans.append(ip_string)
                    return

            for i in range(curr + 1, curr + 4):
                if i > len(s):
                    break
                if i - curr > 1 and s[curr : i].startswith("0"):
                    break
                if int(s[curr : i]) <= 255:
                    recursion(i, dotindices + [i])

        recursion(0)

        return ans
