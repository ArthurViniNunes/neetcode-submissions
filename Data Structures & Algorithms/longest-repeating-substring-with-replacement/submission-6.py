class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        replaces = 0
        l = 0
        r = 1
        while l < len(s):
            if r == len(s):
                prev_l = l
                while l > 0 and replaces < k:
                    replaces += 1
                    l -= 1
                best = max(best, r-l)

                # Se chegar no final
                if prev_l == len(s) - 1:
                    return best

                replaces = 0
                l = prev_l + 1
                r = l

            if s[l] != s[r]:
                replaces += 1
            
            if replaces > k:
                best = max(best, r-l)
                prev = s[l]
                while l < r and prev == s[l]:
                    l += 1
                r = l
                replaces = 0
            
            r += 1
            
            