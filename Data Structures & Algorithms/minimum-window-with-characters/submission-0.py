class Solution:
    def minWindow(self, s: str, t: str) -> str:
        record = {}
        for char in t:
            record[char] = record.get(char, 0) + 1
        
        seen = {}
        l = 0
        ans = ""
        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            if s[r] in record:
                # Se termina com r em s, diminui a janela ao maximo
                while l < r and seen[s[l]] > record.get(s[l], 0):
                    seen[s[l]] -= 1
                    l += 1
                
                # Se record está contido em seen e (ans == "" ou len(ans) > r-l+1)
                contain = True
                for k in record:
                    if record[k] > seen.get(k, 0):
                        contain = False
                
                if contain and (ans == "" or len(ans) > r-l+1):
                    ans = s[l:r+1]
        return ans